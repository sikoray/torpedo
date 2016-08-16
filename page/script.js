$('.multiple-items').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: false,
  nextArrow: '<img src="icons/png/arrow right.png" style="float:right;margin-top:-400px;margin-right:-50px;">',
  prevArrow: '<img src="icons/png/arrow left.png" style="float:left;margin-top:50px;margin-right:20px;">'
});

 
$(document).ready(function(){
	$("#skroll").on("click","a", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();

		//забираем идентификатор бока с атрибута href
		var id  = $(this).attr('href'),

		//узнаем высоту от начала страницы до блока на который ссылается якорь
			top = $(id).offset().top;
		
		//анимируем переход на расстояние - top за 1500 мс
		$('body,html').animate({scrollTop: top}, 1500);
	});
});
