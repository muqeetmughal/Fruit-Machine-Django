import logging

from app.draw import set_code_used, get_prize, get_slot_result, get_prize_result
from app.forms import DrawForm
from app.models import Draw, Prize
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

# Get an instance of a logger
logger = logging.getLogger(__name__)


@csrf_protect
def draw_spin(request):
    logger.info(f"Draw_new with {request.method}")
    prizes = get_list_or_404(Prize)

    if request.method == "POST":
        form = DrawForm(request.POST)

        if form.is_valid():  # and code is valid (checked on form class)
            email = form.cleaned_data['email']
            code = form.cleaned_data['code']
            logger.info(f"email [{email}] code [{code}]")

            r = get_prize_result()
            r1, r2, r3 = get_slot_result(r)
            prize = get_prize(r)

            # Save the draw for logging
            instance = form.save(commit=False)
            instance.date = timezone.now()
            instance.reel1 = r1
            instance.reel2 = r2
            instance.reel3 = r3
            instance.prize = prize
            instance.save()

            # Invalidate the code
            set_code_used(code, True)

            return render(request, 'index.html',
                          {'spin': True,
                           'result': instance.pk,
                           'reel1': instance.reel1,
                           'reel2': instance.reel2,
                           'reel3': instance.reel3,
                           'prizes': prizes})
        else:  # invalid form
            logger.warning(f"invalid form else => {form.is_valid()}")
            logger.warning(f"invalid form else => {form.errors}")
            form = DrawForm(request.POST)
    else:
        form = DrawForm()  # No post data

    return render(request, 'index.html', {'form': form, 'prizes': prizes})


def draw_result(request, pk):
    prizes = get_list_or_404(Prize)
    draw = get_object_or_404(Draw, pk=pk)
    logger.info(f"Draw with {request.method} for id {draw.pk}")

    prize = get_prize(draw.prize.pk)
    logger.info(f"Prize {prize.pk}, {prize.label}, {prize.winner}")

    if prize.try_again:
        set_code_used(draw.code, False)

    return render(request, 'draw.html', {'prizes': prizes, 'result_draw': draw, 'result_prize': prize})


@csrf_protect
def index(request):
    form = DrawForm()
    prizes = get_list_or_404(Prize)

    return render(request, 'index.html', {'form': form, 'prizes': prizes})
