/*! Ithacash.js 2016-01-11 */
$(function(){$("#panels").slick({infinite:!0,autoplay:!0,autoplaySpeed:7e3,prevArrow:$("#left-arrow button"),nextArrow:$("#right-arrow button"),pauseOnHover:!1}).on("afterChange",function(){var a=$(this).slick("slickCurrentSlide");0===a&&$(this).slick("slickPlay")}),$("#intro .banners").slick({autoplay:!0,infinite:!0,autoplaySpeed:5e3,pauseOnHover:!1,dots:!0,appendDots:"#intro-controls"}),$("#more-arrow").click(function(){windowHeight=$(window).height(),sectionHeight=$("#invigorating-our-economy").height(),offset=$("#invigorating-our-economy").offset().top+150-(windowHeight-sectionHeight)/2,$("html, body").animate({scrollTop:offset+"px"})})}),$(function(){$("#nav-menu a").click(function(a){return section=$(this).attr("href"),section.match("#")?(sectionOffset=$(section.replace("/","")).offset().top,scrollTo=sectionOffset-parseInt($("header").css("height")),$("html, body").animate({scrollTop:scrollTo+"px"}),!1):!0}),$("#accounts > ul > li").hover(function(){$("#accounts li").each(function(){$(this).removeClass("selected")}),$(this).addClass("selected"),selection=$(this).attr("id"),$("#"+selection+"-info").toggle(),$("#accounts > div > div").each(function(){$(this).attr("id")!=selection+"-info"?$(this).css("display","none"):$(this).css("display","table-cell")})}),$("#send-message").submit(function(a){a.preventDefault(),data=$(this).serialize(),validation_url=window.location.pathname,$.ajax({url:validation_url,method:"POST",data:data,statusCode:{200:function(){$("#send-message").replaceWith("<p>Thanks for the message!</p>")},400:function(){$("#send-message").append('<p class="error">Please fill out both inputs.</p>')},500:function(){$("#send-message button").replaceWith('<p class="error">An error occured. Please refresh the page and try again.</p>')}}})}),$("#join-email-list").submit(function(a){a.preventDefault(),data=$(this).serialize(),validation_url=window.location.pathname,$.ajax({url:validation_url,method:"POST",data:data,statusCode:{200:function(){$("#join-email-list").replaceWith('<p class="error">Thanks for signing up!</p>')},400:function(a){errors=$.parseJSON(a.responseText),"already exists"==errors.errors?$("#join-email-list").replaceWith('<p class="error">It looks like you&rsquo;re already signed&ndash;up! Check your spam folder if you&rsquo;re not receiving our newsletter.</p>'):$("#join-email-list").append('<p class="error">Please submit your email address.')},500:function(){$("#join-email-list").replaceWith('<p class="error">An error occured. Please refresh the page and try again.</p>')}}})}),$("form.standard-form").submit(function(a){a.preventDefault(),a.stopImmediatePropagation(),form=$(this),data=form.serialize(),action_url=$(this).attr("action"),validation_url=window.location.pathname,$.ajax({url:validation_url,method:"POST",data:data}).always(function(a){console.log(a)}).fail(function(a){return 400==a.status?(errors=$.parseJSON(a.responseText),error_indices=[],$.each(errors,function(a){error_indices.push(a),console.log(a)}),inputs=$(":input",form),$.each(inputs,function(){input_name=$(this).attr("name"),-1!=$.inArray(input_name,error_indices)?(error_message=errors[input_name][0],$(this).next(".error-message").length>0?$(this).next(".error-message").text(error_message):$(this).addClass("error").after('<span class="error-message">'+error_message+"</span>")):($(this).removeClass("error"),$(this).next(".error-message").remove())}),$("html, body").animate({scrollTop:$(".error-message").first().offset().top-170}),!1):void(500==a.status&&$("form#account").replaceWith("<p>An error occured. Please refresh the page and try again.</p>"))}).success(function(){$("form#account").unbind("submit").submit()})})}),$(function(){$("#nav-how-it-works").hover(function(){$("> ul",this).slideDown("fast")},function(){$("> ul",this).slideUp("fast")}),$("#nav-menu ul li ul li ul li").hover(function(){$("> ul",this).length>0&&($(this).css("border-bottom","none"),$("> ul",this).slideDown("fast"))},function(){$("> ul",this).length>0&&($(this).css("border-bottom","none"),$("> ul",this).slideUp("fast"))})});