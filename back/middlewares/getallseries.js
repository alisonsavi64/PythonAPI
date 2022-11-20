const express = require('express')
const axios = require('axios')

const getallseries = function(req, res, next){

        const url = 'http://localhost:5000/api/series/all'
        axios.get(url).then(response => {
                req.data = response.data
                next()
        })

}

module.exports = getallseries
