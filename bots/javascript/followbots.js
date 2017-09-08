//Indicate the bot is running
console.log('twitterbot.js is running');

Already dowload the API package
var Twit = require('twit');
//Twitter account key saved to file called twitterOAUTH and calling here
var twitterOAUTH = require('./twitterOAUTH');

console.log('twitok');

var T = new Twit(twitterOAUTH);

var stream = T.stream('user');
stream.on('follow',followed);

//The followed fucntion
function followed(eventMsg) {
var name = eventMsg.source.name;
var screenName = eventMsg.source.screen_name;
tweetIt('@' + screenName + ' Hi, thanks for following me' );
}

//setInterval(tweetIt, 1000*1);

//tweetIt();

function tweetIt(txt){

//var r = Math.floor(Math.random()*100);
var tweet = {
status: txt
}

T.post('statuses/update', tweet, tweeted);

function tweeted(err,data, response) {
if (err){
console.log("something went wrong!");
} else {
console.log(data)
}
}
}
