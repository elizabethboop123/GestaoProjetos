$(document).ready(function(){
	/*$('.dropdown').dropdown();*/
	$('.vinculo').change(function(){
		$('.vinculo option:selected').each(function(){

			var selecionado = $(this).text();
			if (selecionado.trim() == "Professor"){
				$('.matricula').text('')
				$('.matricula').text('SIAPE')
				$('.periodo').hide()
				$('.curso').hide()
				$('.tres').removeClass('three').removeClass('fields')
			}
			else{
				$('.matricula').text('')
				$('.matricula').text('Matrícula')
				$('.periodo').show()
				$('.curso').show()
				$('.tres').addClass('three').addClass('fields')
			}
		})
		

	})
})
