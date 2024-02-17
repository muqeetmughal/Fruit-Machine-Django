/**
 * Global variables
 */
let completed = 0;
let animationTime = 2500;
let audio = new Audio('static/media/slot.mp3');

/**
 * @class Slot
 * @constructor
 */
function Slot(el, max, step) {
    this.speed = 0; //speed of the slot at any point of time
    this.step = step; //speed will increase at this rate
    this.si = null; //holds setInterval object for the given slot
    this.el = el; //dom element of the slot
    this.maxSpeed = max; //max speed this slot can have
    this.pos = null; //final position of the slot

    $(el).pan({
        fps: 30,
        dir: 'down'
    });
    $(el).spStop();
}

/**
 * @method start
 * Starts a slot
 */
Slot.prototype.start = function () {
    let _this = this;
    $(_this.el).addClass('motion');
    $(_this.el).spStart();
    _this.si = window.setInterval(function () {
        if (_this.speed < _this.maxSpeed) {
            _this.speed += _this.step;
            $(_this.el).spSpeed(_this.speed);
        }
    }, 100);
};

/**
 * @method stop
 * Stops a slot
 */
Slot.prototype.stop = function (r) {
    let _this = this,
        limit = 30;
    clearInterval(_this.si);
    _this.si = window.setInterval(function () {
        if (_this.speed > limit) {
            _this.speed -= _this.step;
            $(_this.el).spSpeed(_this.speed);
        }
        if (_this.speed <= limit) {
            // _this.finalPos(_this.el);
            _this.finalPos(r);
            $(_this.el).spSpeed(0);
            $(_this.el).spStop();
            clearInterval(_this.si);
            $(_this.el).removeClass('motion');
            _this.speed = 0;
        }
    }, 100);
};

/**
 * @method finalPos
 * Finds the final position of the slot
 */
Slot.prototype.finalPos = function (fpos) {
    let el = this.el;
    // let pos = $(el).css('background-position'); //for some unknown reason, this does not work in IE
    let bgPos = "0 " + fpos + "px";

    $(el).animate({
        backgroundPosition: bgPos
    }, {
        duration: 0,
        complete: function () {
            completed++;
        }
    });
};

/**
 * @method reset
 * Reset a slot to initial state
 */
Slot.prototype.reset = function () {
    let el_id = $(this.el).attr('id');
    $._spritely.instances[el_id].t = 0;
    $(this.el).css('background-position', '0px 4px');
    this.speed = 0;
    completed = 0;
    $('#result').html('');
};

//create slot objects
let a = new Slot('#slot1', 30, 1),
    b = new Slot('#slot2', 45, 2),
    c = new Slot('#slot3', 70, 3);

/**
 * Main spin method
 */
function spin(url, r1, r2, r3) {
    console.log("slot.js | spin to", r1, r2, r3);
    playSound()

    // Set a timer to wait the start sound to finish
    window.setTimeout(function () {
        a.start();
        b.start();
        c.start();

        // Stop spinning after 5000 ms
        setTimeout(function () {
            a.stop(r1);
            b.stop(r2);
            c.stop(r3);

            // // Check every 100ms if slots have stopped
            // // If so, enable the control
            // window.setInterval(function () {
            //     if (a.speed === 0 && b.speed === 0 && c.speed === 0 && completed === 3) {
            //         // Jump to result page
            //         window.location.href = url;
            //     }
            // }, 100);

            // Set a timer to wait the sound to finish
            window.setTimeout(function () {
                // Jump to result page
                window.location.href = url;
            }, 2000);
        }, animationTime);
    }, 1000);


}

/**
 * Set all reels to initial state
 */
function setInitialPos() {
    a.reset();
    b.reset();
    c.reset();
}

/**
 * Set all reels to desired state
 */
function setFinalPos(r1, r2, r3) {
    a.finalPos(r1);
    b.finalPos(r2);
    c.finalPos(r3);
}

function playSound() {
    console.log("playSound")

    // Stop and rewind the sound if it already happens to be playing.
    audio.pause();
    audio.currentTime = 0;

    // Play the sound.
    audio.play();
}
