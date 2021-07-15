function validate(){
	var text = document.getElementById("id_text")

	
	if (text.value.length < 5){
		alert("Post Contains atleast 5 characters.")
		text.value=""
		text.focus()
		return false
	}
	return true
	
}