function redirectToProfile(){


        location.href = `/profile`

};

function redirectToSpecificSerie(serie, id){


        location.href = `/addseries/${id}/${serie}`

};

function redirectToLogout(){


        location.href = '/login/logout'

};

function redirectToLogin(){

        location.href = '/login'

};

function redirectToSignup(){

        location.href = '/signup'

};

function redirectToHome(){

        location.href = '/'

};

function deleteUserProfileSerieData(id){

	fetch(`http://localhost:8000/profile/${id}`, {method: 'DELETE'
        }).then(function (response) {

        response.redirected && (location.href = '/profile')
        }).catch(function (err){
                console.warn('Error', err);
        })


}

function updateUserProfileSerieData() {

	const serieData = {

		"watchedEpisodes": document.getElementById('watchedSerieEpisodes').value,
		"watchedSeasons": document.getElementById('watchedSerieSeasons').value,
                "watchedGivedStars": document.getElementById('starsFeedback').value
	
	}

	fetch(`http://localhost:8000/addseries/${document.getElementById('serieProcessUniqueId').value}`, {
	method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify(serieData)

        }).then(function (response) {

        response.redirected && (location.href = `/profile`)
        }).catch(function (err){
                console.warn('Error', err);
        })

}
