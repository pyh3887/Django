/**
 * 
 */


function idCheck(){
	if(regForm.memid.value === ''){
		alert('회원 ID 입력')
		regForm.memid.focus()
	}else{
		url = '/member/idcheck?memid=' + regForm.memid.value
		window.open(url,'memid','toolbar=no,width=300,height=150,top=200,left=300')
	}
	
}

function zipCheck(){
	url = '/member/zipcheck?check=y'
	window.open(url,'zip','toolbar=no,width=600,height=300,top=200,left=300')
	
	
}


function send(zipcode, a1 , a2, a3 ,a4){
	opener.document.regForm.zipcode.value = zipcode
	
	if(a4 === "None") a4 = '';
	
	var addr = a1 + " " + a2 + " " + a3 + "" + a4
	
	opener.document.regForm.address.value = addr 
	
	window.close()
	
}



function inputCheck(){
	if(regForm.memid.value === ""){
		alert('아이디 입력')
		regForm.memid.focus()
		return
	}
	
	if(regForm.passwd.value === ""){
		alert('비밀번호 입력')
		regForm.passwd.focus()
		return
	}
	
	if(regForm.passwd.value !== regForm.passwd.value){
		alert('비밀번호 불일치')
		regForm.repasswd.focus()
		return
		
	}
	
	var regExp = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;

	if (!regForm.email.value.match(regExp) ) {

		alert('email을 입력하세요')

		regForm.email.focus();

		return;

	}

		

	var regExp2 = /^\d{3}-\d{3,4}-\d{4}/;         // 010-111-1234

	if ( !regForm.phone.value.match(regExp2) ) {

		alert('전화번호를 입력하세요')

		regForm.phone.focus();

		return;

	}


	
	regForm.submit();
	
}


