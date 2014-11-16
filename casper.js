#!/usr/bin/env casperjs

var casper = require('casper').create()
var url = casper.cli.args[0]
var width = 1024
var height = 580
var picName = casper.cli.args[1]

casper.start(url, function() {
    this.viewport(width, height)
})

casper.thenOpen(url, function(res) {
    if (res.status >= 400 || res.status == undefined) {
        this.echo('this url is unreachable: ' + res.status)
    } else {
        // this.echo(res.status)
        this.wait(1000, function() {
            this.capture(picName, {
                top: 0,
                left: 0,
                width: width,
                height: height
            })
            this.echo(1)
        })
    }
})

casper.run()
