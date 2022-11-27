const express = require('express')

const axios = require('axios')

const router = express.Router()

router.get('/:userid/:serieid',(req, res) =>{
    
        axios.get(`http://localhost:5000/api/series/${req.params.userid}/${req.params.serieid}`).then(response => {
        if (!req.theresUserCookiesData){     
                  console.log(response.data)
                  res.render("addseries", {serieData: response.data.serieData, userData: undefined})

        }else{
                
                res.render("addseries", {serieData: response.data.serieData, userData: req.userCookiesData })

        }
});
});

router.post('/', (req, res) => {
	const url = 'http://localhost:5000/api/series';

        userAddSerieData = {

                "watchedSerieEpisodes": req.body.watchedSerieEpisodes,
                "watchedSerieSeasons": req.body.watchedSerieSeasons,
		"userId": req.body.userId,
		"serieId": req.body.serieId,
		"starsFeedback": req.body.starsFeedback
		
        };

	axios.post(url, {userAddSerieData,} ).then(response => {
		
		if (Object.keys(response.data).length === 0 && response.data.costructor == undefined){
                  
		  res.send('Série ou Temporada inválida') 
        }else{
                  res.redirect(302, 'profile')

        }

	}).catch((err) => {console.log(err)})
       
});

router.put('/:uniqueid', (req, res) => {
	const specificUniqueIdSerieToUpdate = req.params.uniqueid
	const newUserSerieDataToUpdate = req.body
	axios.put(`http://localhost:5000/api/series/${specificUniqueIdSerieToUpdate}`, {newUserSerieDataToUpdate}).then(response => {
		res.redirect('/profile')	
	})

})

module.exports = router
