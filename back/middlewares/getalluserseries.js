const express = require('express')
const axios = require('axios')

const getalluserseries = function (req, res, next){
        const coo = req.cookies;
        const url = `http://localhost:5000/api/series/seriesuser/${coo.data.user.id}`
        axios.get(url).then(response => {

                req.series = response.data
                next()


})
}

module.exports = getalluserseries
