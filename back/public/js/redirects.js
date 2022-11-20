function rtoprofile(){


        location.href = `/profile`

};

function getserie(serie, id){


        location.href = `/addseries/${id}/${serie}`

};

function logout(){


        location.href = '/login/logout'

};

function login(){

        location.href = '/login'

};

function signup(){

        location.href = '/signup'

};

function home(){

        location.href = '/'

};

function deleteserie(id){

	fetch(`http://localhost:8000/profile/deleteserie/${id}`, {method: 'DELETE'
        }).then(function (response) {

        response.redirected && (location.href = '/profile')
        }).catch(function (err){
                console.warn('Error', err);
        })


}

function updateserie() {

	const data = {
		"epsa": document.getElementById('eps').value,
		"tempsa": document.getElementById('temps').value,
                "stars": document.getElementById('stars').value
	
	}

	fetch(`http://localhost:8000/addseries/update/${document.getElementById('uniqueid').value}`, {
	method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify(data)

        }).then(function (response) {

        response.redirected && (location.href = `/profile`)
        }).catch(function (err){
                console.warn('Error', err);
        })

	



}
