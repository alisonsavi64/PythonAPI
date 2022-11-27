const express = require('express')
const axios = require('axios')

const getAllSeries = function(req, res, next){

        const url = 'http://localhost:5000/api/series'
        axios.get(url).then(response => {
                req.allSeriesData = response.data
                next()
        })

}

module.exports = getAllSeries
