function validate(){
	var fn = document.getElementById('fn')
	var ln = document.getElementById('ln')
	var un = document.getElementById('un')
	var pw1 = document.getElementById('pw1')
	
	var nr = /^[A-Za-z ]+$/

	if (! nr.test(fn.value)) {
		alert("First Name contains only letters")
		fn.value=""
		fn.focus()
		return false
		
	}
	if (fn.value.length < 2){
		alert("Enter your valid name")
		fn.value=""
		fn.focus()
		return false
	
	}
	if (! nr.test(ln.value)) {
		alert("Last Name contains only letters")
		ln.value=""
		ln.focus()
		return false
		
	}
	if (ln.value.length < 2){
		alert("Enter your valid name")
		ln.value=""
		ln.focus()
		return false
	
	}
	if (un.value.length < 4){
		alert("Username contains atleast 5 letters")
		un.value=""
		un.focus()
		return false

	}
	if (pw1.value.length < 5){
		alert("Password length must be more than 5 characters")
		pw1.value=""
		pw1.focus()
		return false
	}
	return true
	
}