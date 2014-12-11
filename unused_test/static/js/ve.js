function helpwords() {

	//with the cool-looking Messi javascript library
	js_data_help = document.getElementById("help");

	new Messi(js_data_help, {title:'Use some of the following words:', width: '390px', center: false, viewport: {top: '420px', left: '13px'}});

}

function disable_submit() {
	//solange nicht auf next geclickt wird: 
	document.getElementById("mySubmit").disabled = true;
    }
	// if we just want to hide the button: document.getElementById("mySubmit").style.display='none';
