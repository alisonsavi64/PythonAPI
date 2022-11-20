const express = require('express')

const axios = require('axios')

const router = express.Router()

router.get('/:userid/:serieid',(req, res) =>{
    
        axios.get(`http://localhost:5000/api/series/seriebyid/${req.params.userid}/${req.params.serieid}`).then(response => {
        if (!req.teste){
                       
                  
                  res.render("addseries", {data: response.data, user: undefined})

        }else{
                
                res.render("addseries", {data: response.data, user: req.cookies.data})

        }
});

});

router.post('/', (req, res) => {
	const url = 'http://localhost:5000/api/series/addseries';

        data = {
                "eps": req.body.eps,
                "temps": req.body.temps,
		"userid": req.body.userid,
		"serieid": req.body.serieid,
		"stars": req.body.stars

		
        };	
	axios.post(url, {data,} ).then(response => {
		console.log(response)
		if (Object.keys(response.data).length === 0 && response.data.costructor == undefined){
                  
		res.send('Série ou Temporada inválida') 
        }else{
                  res.redirect(302, 'profile')

        }

	}).catch((err) => {console.log(err)})
       
});

router.put('/update/:uniqueid', (req, res) => {
	const id = req.params.uniqueid
	const data = req.body
	axios.put(`http://localhost:5000/api/series/updateseries/${id}`, {data}).then(response => {
		res.redirect('/profile')	
	})

})

module.exports = router
