$(document).ready(function() {
    $('#fullpage').fullpage({
        //Navigation
        menu: '#menu',
        lockAnchors: false,
        anchors:['Intro', 'MartiniOne', 'MartiniTwo' , 'MartiniThree', 'MartiniFour', 'DashBoard', 'Disclaimer'],
        navigation: true,
        navigationPosition: 'right',
        //navigationTooltips: ['Intro', 'Facts', 'Vis 1', 'Vis 2', 'Vis 3', 'Moving Forward', 'Recommendations'],
        showActiveTooltip: false,
        slidesNavigation: false,
        slidesNavPosition: 'bottom',

        //Scrolling
        css3: true,
        scrollingSpeed: 700,
        autoScrolling: true,
        fitToSection: true,
        fitToSectionDelay: 1000,
        scrollBar: false,
        easing: 'easeInOutCubic',
        easingcss3: 'ease',
        loopBottom: false,
        loopTop: false,
        loopHorizontal: true,
        continuousVertical: false,
        continuousHorizontal: false,
        scrollHorizontally: false,
        interlockedSlides: false,
        dragAndMove: false,
        offsetSections: false,
        resetSliders: false,
        fadingEffect: false,
        normalScrollElements: '#element1, .element2',
        scrollOverflow: false,
        scrollOverflowReset: false,
        scrollOverflowOptions: null,
        touchSensitivity: 15,
        normalScrollElementTouchThreshold: 5,
        bigSectionsDestination: null,

        //Accessibility
        keyboardScrolling: true,
        animateAnchor: true,
        recordHistory: true,

        //Design
        controlArrows: false,
        verticalCentered: true,
        //sectionsColor : ['#ccc','#ccc', '#ccc', '#ccc'],
        paddingTop: '0em',
        paddingBottom: '10px',
        fixedElements: '#header, .footer',
        responsiveWidth: 0,
        responsiveHeight: 0,
        responsiveSlides: false,
        parallax: false,
        parallaxOptions: {type: 'reveal', percentage: 62, property: 'translate'},

        //Custom selectors
        sectionSelector: '.section',
        slideSelector: '.slide',

        lazyLoading: true,

        //events
        onLeave: function(index, nextIndex, direction){},
        afterLoad: function(anchorLink, index){},
        afterRender: function(){},
        afterResize: function(){},
        afterResponsive: function(isResponsive){},
        afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex){

            console.log(anchorLink, index, slideAnchor, slideIndex);
            if(anchorLink === 'MartiniOne'){
                CourseCount();

            }
        },

        onSlideLeave: function(anchorLink, index, slideIndex, direction, nextSlideIndex){}
    });
});


// on new info - update vis!