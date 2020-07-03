// Initialization of external libraries

if (Boolean(document.querySelector('.popbox'))) {
    var popbox = new Popbox();
}

(function () {
    if (Boolean(document.querySelector('.js-slider'))) {
        document.querySelectorAll(".js-slider").forEach(slider => {
            tns({
                "container": slider,
                "mouseDrag": true,
                "autoplay": true,
                "autoplayTimeout": 7000,
                "autoplayHoverPause": true,
                "autoplayText": ["", ""],
                "gutter": 15,
                "controlsText": ["", ""],
                "navPosition": "bottom",
                "loop": true,
                "autoHeight": true,
            })
        });
    }

    if (Boolean(document.querySelector('.js-slider-gallery'))) {
        if (window.innerWidth > 1400) {
            document.querySelectorAll(".js-slider-gallery").forEach(slider => {
                preprocessGallerySlider(slider, 5);
            });
        }

        if ((window.innerWidth > 1250) && (window.innerWidth <= 1400)) {
            document.querySelectorAll(".js-slider-gallery").forEach(slider => {
                preprocessGallerySlider(slider, 4);
            })
        }

        if (window.innerWidth <= 500) {
            document.querySelectorAll(".slider-gallery__item").forEach(item => {
                makeOneImagePerSlide(item);
            });
        }

        document.querySelectorAll(".js-slider-gallery").forEach(slider => {
            let controls = slider.closest(".js-slider-gallery-container").querySelector(".js-slider-gallery__controls");
            tns({
                "container": slider,
                "items": 1,
                "slideBy": "page",
                "mode": "gallery",
                "gutter": 0,
                "animateIn": "slider-gallery-animation-in",
                "animateOut": "slider-gallery-animation-out",
                "mouseDrag": true,
                "controlsContainer": controls,
                "nav": false,
                "loop": true,
                responsive: {
                    1401: {
                        "items": 5,
                    },
                    1251: {
                        "items": 4,
                    },
                    501: {
                        "items": 2,
                    }
                }
            });
        });
    }

    if (Boolean(document.querySelector('.slider-lineup'))) {
        document.querySelectorAll(".slider-lineup").forEach(slider => {
            let slider__nav = slider.closest('.container').querySelector('.slider-lineup-nav');
            tns({
                "container": slider,
                "items": 1,
                "slideBy": "page",
                "mode": "gallery",
                "gutter": 0,
                "animateIn": "slider-gallery-animation-in",
                "animateOut": "slider-gallery-animation-out",
                "mouseDrag": false,
                "touch": false,
                "navContainer": slider__nav,
                "loop": true,
            });
        })
    }


    if (Boolean(document.querySelector('[data-tabs]'))) {
        new Tabby('[data-tabs]');
    }

    if (Boolean(document.querySelector('select'))) {
        document.querySelectorAll('select').forEach(select => {
            easydropdown(select)
        })

    }

    if (Boolean(document.querySelector('.js-about-article')) && window.innerWidth < 600) {
        $readMoreJS.init({
            target: '.js-about-article',
            numOfWords: 55,
            toggle: false,
            moreLink: 'читать',
        });
    }

    /**
     * make every slide to contain only 1 image
     * @param  {Node} slider Gallery slider i.e. multiple slides on one page
     * @param  {number} insertAfterIndexIncrement How much slides on one page including dummy slides?
     */
    function preprocessGallerySlider(slider, insertAfterIndexIncrement) {
        let numberOfSlides = slider.children.length;
        let insertAfterIndex = 2;
        let processingIndex = 0;
        for (processingIndex; processingIndex < numberOfSlides; processingIndex++) {
            if (processingIndex === insertAfterIndex) {  // add dummy slide
                slider.children[insertAfterIndex].insertAdjacentHTML('afterend', '<div></div>');
                insertAfterIndex += insertAfterIndexIncrement;
                numberOfSlides += 1;
            }
        }

        processingIndex = numberOfSlides - 1;
        let indexOfAdditionalSlide = 0;
        while (numberOfSlides % insertAfterIndexIncrement != 0) {
            if (processingIndex === insertAfterIndex) {  // add dummy slide
                slider.children[insertAfterIndex].insertAdjacentHTML('afterend', '<div></div>');
                insertAfterIndex += insertAfterIndexIncrement;
                numberOfSlides += 1;
            } else {  // fill empty space with slides
                slider.appendChild(slider.children[indexOfAdditionalSlide].cloneNode(true));
                numberOfSlides += 1;
                indexOfAdditionalSlide += 1;
            }
            processingIndex += 1;
        }
    }


    /**
     * make every slide to contain only 1 image
     * @param  {Node} item Slide that can contain 1 or 2 images
     */
    function makeOneImagePerSlide(item) {
        let imgs = item.children;
        if (imgs.length > 1) {
            let newItem = document.createElement("div");
            let img = imgs[0];
            newItem.appendChild(img.cloneNode(true));
            let slider = img.closest(".js-slider-gallery");
            slider.insertBefore(newItem, item);
            img.remove()
        }
    }
}());


(function () {
    if (Boolean(document.querySelector('.bg-video-section.js-bg-video-section'))) {
        dimVideoSection();
        document.querySelector('.js-bg-video-section__video').play();
        window.addEventListener('scroll', function () {
            dimVideoSection()
        });

        function dimVideoSection() {
            let element = document.querySelector(".js-bg-video-section__overflow");
            let windowBottom = window.pageYOffset + window.innerHeight;
            let elementTop = element.offsetTop;
            let percentage = ((windowBottom - elementTop) / element.offsetHeight) * 0.7;

            if (percentage < 0.4) {
                percentage = 0.4
            } else if (percentage > 0.8) {
                percentage = 0.8;
            }
            element.style.opacity = String(percentage);
        }
    }
}());

document.querySelectorAll(".js-callback-btn").forEach(btn => {
    btn.addEventListener("click", function (e) {
        e.preventDefault();

        let forms = document.querySelectorAll("form");
        let form = this.closest("form");
        let formIndex = [...forms].indexOf(form);  // get index of form (need for validating recaptcha)

        let csrfValue = form.querySelector("input[name=csrfmiddlewaretoken]").value;
        let nameInput = form.querySelector("input[name=name]");
        let nameValue = nameInput.value;
        let isNameValid = validateName(nameValue);
        let phoneInput = form.querySelector("input[name=phone]");
        let phoneValue = phoneInput.value;
        let isPhoneValid = validatePhone(phoneValue);

        let whenToCallValue = "—";
        let emailValue = "—";
        let isEmailValid = true;

        if (Boolean(form.querySelector("select[name=when-to-call]"))) {
            whenToCallValue = form.querySelector("select[name=when-to-call]").value;
        }

        if (Boolean(form.querySelector("input[name=email]"))) {
            let emailInput = form.querySelector("input[name=email]");
            emailValue = emailInput.value;
            isEmailValid = validateEmail(emailValue);
            if (!isEmailValid) inputErrorAnimation(emailInput);
        }

        if (!isNameValid) inputErrorAnimation(nameInput);
        if (!isPhoneValid) inputErrorAnimation(phoneInput);

        if (!isCaptchaChecked(formIndex)) inputErrorAnimation(form.querySelector(".g-recaptcha"));

        let isFormValid = isEmailValid && isPhoneValid && isNameValid && isCaptchaChecked(formIndex);

        if (isFormValid) {

            postAjax('callback/record_callback/', {
                csrfmiddlewaretoken: csrfValue,
                name: nameValue,
                phone: phoneValue,
                whenToCall: whenToCallValue,
                email: emailValue
            }, function (data) {
                // console.log("success", data);
            });
            form.reset();
            grecaptcha.reset(formIndex);
            popbox.close(form.closest(".popbox"));
            popbox.open("popbox-callback-success")
        }

    });
});


document.addEventListener("click", function (e) {
    if (e.target.matches('.js-video-gallery-ajax-link') || e.target.closest('.js-video-gallery-ajax-link')) {
        e.preventDefault();

        if (e.target.matches('.tab-title__link')) {
            document.querySelectorAll('.tab-title__link').forEach(tab_title => {
                tab_title.setAttribute('aria-selected', false)
            });
            e.target.setAttribute('aria-selected', true);
        }

        let link = e.target.closest('.js-video-gallery-ajax-link');
        let page_url_part = link.getAttribute('href');
        let page_url = 'http://127.0.0.1:8000' + page_url_part;
        let content_container = document.querySelector('.tab-content__item');

        fadeOut(content_container.querySelector('div'), 500);

        // while (content_container.firstChild) content_container.removeChild(content_container.firstChild);

        getAjax(page_url, function (data) {
            video_gallery_ajax_success(data, content_container);
        });

        history.pushState(null, '', page_url_part);
    }
}, false);

document.addEventListener("click", function (e) {
    if (e.target.matches('.js-photo-gallery-ajax-link') || e.target.closest('.js-photo-gallery-ajax-link')) {
        e.preventDefault();

        if (e.target.matches('.tab-title__link')) {
            document.querySelectorAll('.tab-title__link').forEach(tab_title => {
                tab_title.setAttribute('aria-selected', false)
            });
            e.target.setAttribute('aria-selected', true);
        }

        let link = e.target.closest('.js-photo-gallery-ajax-link');
        let page_url_part = link.getAttribute('href');
        let page_url = 'http://127.0.0.1:8000' + page_url_part;
        let content_container = document.querySelector('.tab-content__item');

        fadeOut(content_container.querySelector('div'), 500);

        // while (content_container.firstChild) content_container.removeChild(content_container.firstChild);

        getAjax(page_url, function (data) {
            photo_gallery_ajax_success(data, content_container)
        });


        history.pushState(null, '', page_url_part);

        // window.onpopstate = function(e){
        // getAjax(document.location, function (data) {
        //     photo_gallery_ajax_success(data, content_container)
        // });
        // window.location.reload();
        // };
    }
}, false);
if (Boolean(document.querySelector('.pagination'))) {
    document.querySelectorAll('.pagination')[1].classList.add('pagination_has-large-padding_top');
}

function video_gallery_ajax_success(data, content_container) {
    let jsonData = JSON.parse(data);
    let video_items = "";
    jsonData.forEach(video => {
        let title = video.title;
        let video_id = video.video_id;
        let properties = video.properties;
        let property_rows = "";


        properties.forEach(property_item => {
            property_rows += '<div class="video-gallery__property-row">' +
                '<div class="video-gallery__property">' + property_item.property + '</div>' +
                '<div class="video-gallery__description">' + property_item.description + '</div>' +
                '</div>'
        });

        video_items += '<div class="video-gallery__item">' +
            '<div class="video-gallery__title">' + title + '</div>' +
            '<div class="video-gallery__grid">' +
            '<div class="video-gallery__player"><iframe class="video-gallery__iframe" width="100%" height="100%"' +
            'src="https://www.youtube.com/embed/' + video_id + '?rel=0&amp;amp;&amp;amp;showinfo=0"' +
            'frameborder="0"></iframe></div>' + // video-gallery__player
            '<div class="video-gallery__sidebar"><div class="video-gallery__property-list">' + property_rows + '</div>' +
            '<a class="video-gallery__btn btn btn_primary" href="/callback/">Хочу также</a></div>' + // video-gallery__sidebar
            '</div>' + // video-gallery__grid
            '</div>';  // video-gallery__item
    });

    content_container.innerHTML = jsonData[0]['pagination_html'] +
        '<div class="video-gallery">' + video_items + '</div>' +
        jsonData[0]['pagination_html'];


    if (Boolean(document.querySelector('.gallery-page .pagination'))) {
        document.querySelectorAll('.gallery-page .pagination')[1].classList.add('pagination_has-large-padding_top');
    }
}

function photo_gallery_ajax_success(data, content_container) {
    let jsonData = JSON.parse(data);
    let figures = "";
    jsonData.forEach(photo => {
        let picture = photo.picture;
        let thumbnail = photo.thumbnail;
        let caption = photo.caption;
        let size = photo.size;

        figures += '<figure class="photo-gallery__item">' +
            '<a class="photo-gallery__img" href="' + picture + '" data-size=' + size + '> ' +
            '<img class="photo-gallery__thumbnail" src="' + thumbnail + '" alt="Надпись"></a> ' +
            '<figcaption class="photo-gallery__caption">' + caption + '</figcaption> ' +
            '</figure>';
    });

    content_container.innerHTML = jsonData[0]['pagination_html'] +
        '<div class="photo-gallery js-photo-gallery photo-gallery_has-padding_top">' + figures + '</div>' +
        jsonData[0]['pagination_html'];

    initPhotoSwipeFromDOM('.js-photo-gallery');  // reinit photoSwipe

    if (Boolean(document.querySelector('.gallery-page .pagination'))) {
        document.querySelectorAll('.gallery-page .pagination')[1].classList.add('pagination_has-large-padding_top');
    }
}

// fade an element from the current state to full opacity in "duration" ms
function fadeOut(el, duration) {
    var s = el.style, step = 25 / (duration || 300);
    s.opacity = s.opacity || 1;
    (function fade() {
        (s.opacity -= step) < 0 ? s.display = "none" : setTimeout(fade, 25);
    })();
}

// fade out an element from the current state to full transparency in "duration" ms
// display is the display style the element is assigned after the animation is done
function fadeIn(el, duration, display) {
    var s = el.style, step = 25 / (duration || 300);
    s.opacity = s.opacity || 0;
    s.display = display || "block";
    (function fade() {
        (s.opacity = parseFloat(s.opacity) + step) > 1 ? s.opacity = 1 : setTimeout(fade, 25);
    })();
}

function postAjax(url, data, success) {
    let params = typeof data == 'string' ? data : Object.keys(data).map(
        function (k) {
            return encodeURIComponent(k) + '=' + encodeURIComponent(data[k])
        }
    ).join('&');

    let xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
    xhr.open('POST', url);
    xhr.onreadystatechange = function () {
        if (xhr.readyState > 3 && xhr.status === 200) {
            success(xhr.responseText);
        }
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send(params);
    return xhr;
}

function getAjax(url, success) {
    let xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
    xhr.open('GET', url);
    xhr.onreadystatechange = function () {
        if (xhr.readyState > 3 && xhr.status === 200) success(xhr.responseText);
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.send();
    return xhr;
}


function validatePhone(inputPhoneValue) {
    return !!(inputPhoneValue.length === 15);
}

function validateEmail(inputEmailValue) {
    let mail_format = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return !!inputEmailValue.match(mail_format);
}

function validateName(inputNameValue) {
    let name_format = /^[A-Za-z\u0400-\u04FF\s]+$/;
    return !!inputNameValue.match(name_format);
}

function isCaptchaChecked(captchaId) {
    return grecaptcha && grecaptcha.getResponse(captchaId).length !== 0;
}

function inputErrorAnimation(input) {
    input.classList.add("bounce");
    setTimeout(function () {
        input.classList.remove("bounce");
    }, 1000);
}


(function () {
    let burger = document.querySelector(".js-burger");
    let headerNavContainer = document.querySelector(".header-nav-container");
    let header = document.querySelector(".header");
    let html = document.querySelector("html");

    document.addEventListener('click', function (e) {
        let area = e.target;

        let areaArray = [];
        while (area) {
            areaArray.unshift(area);
            area = area.parentElement;
        }

        let hasBurgerParent = areaArray.some(function (num) {
            return num.classList.contains("burger");
        });

        let hasHeaderNavActiveParent = areaArray.some(function (num) {
            return num.classList.contains("header-nav-container_active");
        });

        let hasHeaderNavLinkParent = areaArray.some(function (num) {
            return num.classList.contains("header-nav__link");
        });

        if (hasBurgerParent) {
            burger.classList.toggle("burger_active");
            headerNavContainer.classList.toggle("header-nav-container_active");

            if (window.innerWidth < 1050) {
                header.classList.toggle("header_in-menu");
                html.classList.toggle("popbox_locked");
            }
        } else if (!hasHeaderNavActiveParent) {
            burger.classList.remove("burger_active");
            headerNavContainer.classList.remove("header-nav-container_active");
        }
        if (hasHeaderNavLinkParent) {
            burger.classList.remove("burger_active");
            headerNavContainer.classList.remove("header-nav-container_active");
            header.classList.remove("header_in-menu");
            html.classList.remove("popbox_locked");
        }

    });

}());
(function () {
    if (Boolean(document.querySelector('input[name=phone]'))) {
        document.querySelectorAll("input[name=phone]").forEach(input => {
            input.addEventListener("input", mask, false);
            input.addEventListener("focus", mask, false);
            input.addEventListener("blur", mask, false);
        });
    }

    function setCursorPosition(pos, elem) {
        elem.focus();
        if (elem.setSelectionRange) elem.setSelectionRange(pos, pos);
        else if (elem.createTextRange) {
            let range = elem.createTextRange();
            range.collapse(true);
            range.moveEnd("character", pos);
            range.moveStart("character", pos);
            range.select();
        }
    }

    function mask(event) {
        let matrix = "_ ___ ___ __ __",
            i = 0,
            def = matrix.replace(/\D/g, ""),
            val = this.value.replace(/\D/g, "");
        if (def.length >= val.length) val = def;
        this.value = matrix.replace(/./g, function (a) {
            return /[_\d]/.test(a) && i < val.length
                ? val.charAt(i++)
                : i >= val.length ? "" : a;
        });
        if (event.type === "blur") {
            if (this.value.length === 2) this.value = "";
        } else setCursorPosition(this.value.length, this);
    }
})();

var initPhotoSwipeFromDOM = function (gallerySelector) {

    // parse slide data (url, title, size ...) from DOM elements
    // (children of gallerySelector)
    var parseThumbnailElements = function (el) {
        var thumbElements = el.childNodes,
            numNodes = thumbElements.length,
            items = [],
            figureEl,
            linkEl,
            size,
            item;

        for (var i = 0; i < numNodes; i++) {

            figureEl = thumbElements[i]; // <figure> element

            // include only element nodes
            if (figureEl.nodeType !== 1) {
                continue;
            }

            linkEl = figureEl.children[0]; // <a> element

            size = linkEl.getAttribute('data-size').split('x');

            // create slide object
            item = {
                src: linkEl.getAttribute('href'),
                w: parseInt(size[0], 10),
                h: parseInt(size[1], 10)
            };


            if (figureEl.children.length > 1) {
                // <figcaption> content
                item.title = figureEl.children[1].innerHTML;
            }

            if (linkEl.children.length > 0) {
                // <img> thumbnail element, retrieving thumbnail url
                item.msrc = linkEl.children[0].getAttribute('src');
            }

            item.el = figureEl; // save link to element for getThumbBoundsFn
            items.push(item);
        }

        return items;
    };

    // find nearest parent element
    var closest = function closest(el, fn) {
        return el && (fn(el) ? el : closest(el.parentNode, fn));
    };

    // triggers when user clicks on thumbnail
    var onThumbnailsClick = function (e) {
        e = e || window.event;
        e.preventDefault ? e.preventDefault() : e.returnValue = false;

        var eTarget = e.target || e.srcElement;

        // find root element of slide
        var clickedListItem = closest(eTarget, function (el) {
            return (el.tagName && el.tagName.toUpperCase() === 'FIGURE');
        });

        if (!clickedListItem) {
            return;
        }

        // find index of clicked item by looping through all child nodes
        // alternatively, you may define index via data- attribute
        var clickedGallery = clickedListItem.parentNode,
            childNodes = clickedListItem.parentNode.childNodes,
            numChildNodes = childNodes.length,
            nodeIndex = 0,
            index;

        for (var i = 0; i < numChildNodes; i++) {
            if (childNodes[i].nodeType !== 1) {
                continue;
            }

            if (childNodes[i] === clickedListItem) {
                index = nodeIndex;
                break;
            }
            nodeIndex++;
        }


        if (index >= 0) {
            // open PhotoSwipe if valid index found
            openPhotoSwipe(index, clickedGallery);
        }
        return false;
    };

    // parse picture index and gallery index from URL (#&pid=1&gid=2)
    var photoswipeParseHash = function () {
        var hash = window.location.hash.substring(1),
            params = {};

        if (hash.length < 5) {
            return params;
        }

        var vars = hash.split('&');
        for (var i = 0; i < vars.length; i++) {
            if (!vars[i]) {
                continue;
            }
            var pair = vars[i].split('=');
            if (pair.length < 2) {
                continue;
            }
            params[pair[0]] = pair[1];
        }

        if (params.gid) {
            params.gid = parseInt(params.gid, 10);
        }

        return params;
    };

    var openPhotoSwipe = function (index, galleryElement, disableAnimation, fromURL) {
        var pswpElement = document.querySelectorAll('.pswp')[0],
            gallery,
            options,
            items;

        items = parseThumbnailElements(galleryElement);

        // define options (if needed)
        options = {

            // define gallery index (for URL)
            galleryUID: galleryElement.getAttribute('data-pswp-uid'),
            showHideOpacity: true,
            shareEl: false,

        };

        // PhotoSwipe opened from URL
        if (fromURL) {
            if (options.galleryPIDs) {
                // parse real index when custom PIDs are used
                // http://photoswipe.com/documentation/faq.html#custom-pid-in-url
                for (var j = 0; j < items.length; j++) {
                    if (items[j].pid == index) {
                        options.index = j;
                        break;
                    }
                }
            } else {
                // in URL indexes start from 1
                options.index = parseInt(index, 10) - 1;
            }
        } else {
            options.index = parseInt(index, 10);
        }

        // exit if index not found
        if (isNaN(options.index)) {
            return;
        }

        if (disableAnimation) {
            options.showAnimationDuration = 0;
        }

        // Pass data to PhotoSwipe and initialize it
        gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
        gallery.init();
    };

    // loop through all gallery elements and bind events
    var galleryElements = document.querySelectorAll(gallerySelector);

    for (var i = 0, l = galleryElements.length; i < l; i++) {
        galleryElements[i].setAttribute('data-pswp-uid', i + 1);
        galleryElements[i].onclick = onThumbnailsClick;
    }

    // Parse URL and open gallery if it contains #&pid=3&gid=1
    var hashData = photoswipeParseHash();
    if (hashData.pid && hashData.gid) {
        openPhotoSwipe(hashData.pid, galleryElements[hashData.gid - 1], true, true);
    }
};

// execute above function
initPhotoSwipeFromDOM('.js-photo-gallery');


(function () {
    let burgerNav = document.querySelector(".js-burger-nav");
    let callSpecialistBtn = document.querySelector(".js-header__call-specialist-btn");
    let header = document.querySelector(".js-header");
    let subheader = document.querySelector(".js-subheader");
    let headerHeight = header.offsetHeight;
    let subheaderHeight = subheader.offsetHeight;
    let stickyOffset = headerHeight + subheaderHeight + 50;
    let html = document.querySelector("html");

    if (window.pageYOffset > stickyOffset) {
        header.classList.add("header_sticky");
        burgerNav.classList.remove("h-hide");
        callSpecialistBtn.classList.remove("h-hide");
        html.style.marginTop = headerHeight + "px";
    } else {
        header.classList.remove("header_sticky");
        burgerNav.classList.add("h-hide");
        callSpecialistBtn.classList.add("h-hide");
        html.style.marginTop = 0 + "px";
    }

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > stickyOffset) {
            header.classList.add("header_sticky");
            burgerNav.classList.remove("h-hide");
            callSpecialistBtn.classList.remove("h-hide");
            html.style.marginTop = headerHeight + "px";
        } else {
            header.classList.remove("header_sticky");
            burgerNav.classList.add("h-hide");
            callSpecialistBtn.classList.add("h-hide");
            html.style.marginTop = 0 + "px";
        }
    });

}());
let tagForYoutubeApi = document.createElement('script');
tagForYoutubeApi.src = "https://www.youtube.com/iframe_api";
let firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tagForYoutubeApi, firstScriptTag);

/**
 * Change playing video by clicking on thumbnail and swap thumbnails
 */
function onYouTubeIframeAPIReady() {
    if (Boolean(document.querySelector('.js-video-feedback-gallery'))) {
        let playerContainer = document.querySelector(".js-video-feedback-gallery__player-container");
        let currentVideoYoutubeId = playerContainer.getAttribute("data-js-video-youtube-id");
        let currentVideoThumbnail = playerContainer.getAttribute("data-js-video-thumbnail");
        let nextVideoYoutubeId = "";
        let nextVideoThumbnail = "";

        let player = new YT.Player("js-video-feedback-gallery-player-placeholder", {
            videoId: currentVideoYoutubeId,
            height: "100%",
            width: "100%"
        });

        document.querySelectorAll(".js-video-feedback-gallery__thumbnail-container").forEach(thumbnailContainer => {
            thumbnailContainer.addEventListener("click", function () {
                nextVideoYoutubeId = this.getAttribute("data-js-video-youtube-id");
                nextVideoThumbnail = this.getAttribute("data-js-video-thumbnail");
                playerContainer.setAttribute("data-js-video-youtube-id", nextVideoYoutubeId);
                playerContainer.setAttribute("data-js-video-thumbnail", nextVideoThumbnail);

                this.setAttribute("data-js-video-youtube-id", currentVideoYoutubeId);
                this.setAttribute("data-js-video-thumbnail", currentVideoThumbnail);

                let thumbnail = this.querySelector(".js-video-feedback-gallery__thumbnail");
                thumbnail.src = currentVideoThumbnail;

                currentVideoYoutubeId = nextVideoYoutubeId;
                currentVideoThumbnail = nextVideoThumbnail;

                player.loadVideoById(nextVideoYoutubeId);
            })
        });
    }
}

(function () {
    if (Boolean(document.querySelector('.js-accordion__title'))) {
        document.querySelectorAll(".js-accordion__title").forEach(accordion => {
            accordion.addEventListener("click", function () {
                this.classList.toggle("accordion__title_active");
                let accordion = this.closest(".js-accordion");
                let accordion__content = accordion.querySelector(".js-accordion__content");
                if (accordion__content.style.maxHeight) {
                    accordion__content.style.maxHeight = null;
                } else {
                    accordion__content.style.maxHeight = accordion__content.scrollHeight + "px";
                }
            });
        });
    }
}());