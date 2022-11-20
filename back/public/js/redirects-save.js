function rtoprofile(){

        fetch(`http://localhost:8000/profile/r`, {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = `/profile/r`)
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function getserie(serie, id){

	console.log('entrei')
        fetch(`http://localhost:8000/addseries/${id}/${serie}`, {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = `/addseries/${id}/${serie}`)
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function logout(){

        fetch('http://localhost:8000/login/logout', {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = '/login/logout')
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function login(){

        fetch('http://localhost:8000/login/r', {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = '/login/r')
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function signup(){

        fetch('http://localhost:8000/signup/r', {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = '/signup/r')
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function home(){

        fetch('http://localhost:8000/r', {method: 'GET'
        }).then(function (response) {

        response.redirected && (location.href = '/r')
        }).catch(function (err){
                console.warn('Error', err);
        })

};

function deleteserie(id){

	fetch(`http://localhost:8000/profile/deleteserie/${id}`, {method: 'DELETE'
        }).then(function (response) {

        response.redirected && (location.href = '/profile/r')
        }).catch(function (err){
                console.warn('Error', err);
        })


}

function updateserie() {

	const data = {
		"epsa": document.getElementById('eps').value,
		"tempsa": document.getElementById('temps').value
	
	}

	fetch(`http://localhost:8000/addseries/update/${document.getElementById('uniqueid').value}`, {
	method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify(data)

        }).then(function (response) {

        response.redirected && (location.href = `/profile/r`)
        }).catch(function (err){
                console.warn('Error', err);
        })

	



}
