//welcome message function

$( document ).ready(function() {
    console.log( "ready!" );
    speechRs.speechinit('Google हिन्दी',function(e){
	        speechRs.speak("Hi, I am Alexaa.", function() {
                   //speaking completed.
               }, false);	
//recording function called
        recording();
      });
    

});

//now app will listen to user response
function recording(){
    speechRs.rec_start('en-IN',function(final_transcript){
      var convertedText=final_transcript.toLowerCase();
        console.log(final_transcript);
        speechRs.rec_stop();
        //function for ajax request
        requestintro(convertedText);
    });   
}
      


//ajax req sent to wit.ai and response received
  function requestintro(convertedText){
        $.ajax({
                    url: 'https://api.wit.ai/message',
                    data: {
                    'q': convertedText,
                    'access_token' : 'QW5T3QZR46XQKLKJKCXSDWG6MESMYSIO'
                    },
                    dataType: 'jsonp',
                    method: 'GET',
                    success: function(response) {
                        console.log("success!", response);
                        if(response.entities.intent[0].value == 'hello') {
                           //function called
                            sayHi();
                        }
                        else if(response.entities.search_query[0].value == 'hi') {
                            //function called
                            sayHi() ;
                        }
                    }
            
                });

  }
                        
                    
    


//tells user to proceed
function sayHi(){
        
    speechRs.speechinit('Google हिन्दी',function(e){
                speechRs.speak("Hi, sir. Please login to continue.", function() {
                    //speaking completed.
                 }, false);	
});
                
}






var two=false;
//click function trggers on clicking login button 

$('#change').on('click', function() {
var name=$('#usr').val();
var passward=$('#pwd').val();     
if(name.length>3 && passward.length>5)
{          
var user=name;
$('.username').text(user);
$('#first').addClass('hidden');
$('#two').removeClass('hidden');
var two=true;
    if(two==true){
        allMoods();
        console.log("allMoods() Called")
    }
$('#search').addClass('hidden');
    
//bot asks user for mood playlist
    
var welcomeGreeting="Welcome,"+name+". What should I play For You?";
var moodList=", Romantic Songs, English Songs, INDO-POP, Old IS Gold, Bollywood Mashups, Party Songs"
     speechRs.speechinit('Google हिन्दी',function(e){
	        speechRs.speak(welcomeGreeting, function() {
                   //speaking completed.
               }, false);	  
     });
     speechRs.speechinit('Google हिन्दी',function(e){
	        speechRs.speak(moodList, function() {
                   //speaking completed.
               }, false);
       
     });
    
     moodRecord();
      
  
}
else{
alert('Enter valid Username and Password.');
}

});



//on clicking any mood it jumps to playlist

function moodload(){
for(i=0;i<6;i++){
    var moodnumber=".mood"+(i+1);
    $(moodnumber).on('click',function(){
    $('#mood').addClass('hidden');
    $('#player-list').removeClass('hidden');
    $('#piano').removeClass('hidden');
    $('#drum').removeClass('hidden');
    $('#search').removeClass('hidden');
});
}
}
//triggers automatically
moodload();



//play pause toggling function

function toggleSong() {
    var song=document.querySelector('audio');
    if(song.paused==true){
        $('.play-icon').removeClass('fa-play').addClass('fa-pause');
        song.play();
        console.log('playing');
    }
    else{
        $('.play-icon').removeClass('fa-pause').addClass('fa-play');
        song.pause();
        console.log('paused');
        
    }
} 

$('.fa-play').on('click',function(){
 toggleSong();
});


$('body').on('keypress',function(event){
   if (event.keyCode==32 ){
      toggleSong();
   } 
});

//used for displaying accurate time
function fancyTimeFormat(time)
{   
    // Hours, minutes and seconds
    var hrs = ~~(time / 3600);
    var mins = ~~((time % 3600) / 60);
    var secs = time % 60;

    // Output like "1:01" or "4:03:59" or "123:03:59"
    var ret = "";

    if (hrs > 0) {
        ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
    }

    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
}


//function to check song duration
function songduration(){
    var song=document.querySelector('audio');
    var currentTime = Math.floor(song.currentTime);         //removes decimal value
    currentTime = fancyTimeFormat(currentTime);             //passes current time format to fancy formare

    var duration = Math.floor(song.duration);
    duration = fancyTimeFormat(duration)

    $('.currentTime').text(currentTime);
    $('.duration').text(duration);
    
}


//object details inside array for every mood load

var romantic = [{
        'name': 'Ae Dil Hai Mushkil',
        'artist': 'Arijit Singh, Pritam',
        'album': 'Ae Dil Hai Mushkil',
        'duration': '4:29',
       'fileName': 'romantic1.mp3',
       'image':'aedil.jpg'
    },
    {
        'name': 'Aaj Zid',
        'artist': 'Arijit Singh',
        'album': 'Aksar 2',
        'duration': '4:12',
        'fileName': 'romantic2.mp3',
        'image':'aajzid.jpg'
    },
    {
        'name': 'Janna Ve',
        'artist': 'Arijit Singh',
        'album': 'Aksar 2',
        'duration': '5:33',
        'fileName': 'romantic3.mp3',
        'image':'jannave.jpg'
    },
    {
        'name': 'Meer-E-Karawan',
        'artist': 'Amit Mishra, Neeti Mohan',
        'album': 'Luckhnow Central',
        'duration': '6:03',
        'fileName': 'romantic4.mp3',
        'image':'meere.jpg'
    }]

var english = [{
        'name': 'Closer',
        'artist': 'The Chainsmokers ft. Halsey',
        'album': 'Collage',
        'duration': '4:21',
       'fileName': 'english1.mp3',
        'image':'closer.png'
    },
    {
        'name': 'Despacito',
        'artist': 'Luis Fonsi, Daddy Yankee ft. Justin Bieber',
        'album': 'Singles',
        'duration': '3:49',
        'fileName': 'english2.mp3',
        'image':'despacito.jpg'
    },
    {
        'name': 'Let Me Love You',
        'artist': 'Dj Snake Ft. Justin Bieber',
        'album': 'Encore',
        'duration': '3:26',
        'fileName': 'english3.mp3',
        'image':'letme.png'
    },
    {
        'name': 'Shape Of You',
        'artist': 'Ed Sheeran',
        'album': '÷',
        'duration': '3:53',
        'fileName': 'english4.mp3',
        'image':'shape.jpg'
    }]

var indopop = [{
        'name': 'Closer-Kabira',
        'artist': 'Vidya Vox',
        'album': 'Vidya Vox Mashup',
        'duration': '3:23',
       'fileName': 'indopop1.mp3',
       'image':'closerkabira.jpg'
    },
    {
        'name': 'Coldplay n Channa Mereya ',
        'artist': 'Vidya Vox',
        'album': 'Vidya Vox Mashup ',
        'duration': '3:06',
        'fileName': 'indopop2.mp3',
        'image':'coldplaynchanna.jpg'
    },
    {
        'name': 'Let Me n Tum  Hi Ho',
        'artist': 'Vidya Vox',
        'album': 'Let me love you n Tum hi ho',
        'duration': '3:10',
        'fileName': 'indopop3.mp3',
        'image':'letntum.jpg'
    },
    {
        'name': 'Shape Of You(Mann Mera)',
        'artist': 'Gajendra Verma, Ed Sheraan',
        'album': 'Shape of you(Mann Mera)',
        'duration': '3:54',
        'fileName': 'indopop4.mp3',
        'image':'shapenmann.jpg'
    }]

var oldgold = [{
        'name': 'Pehla Nasha',
        'artist': 'Udit Narayan, Sadhna Sargam',
        'album': 'Jo Jeeta Wohi Sikandar',
        'duration': '4:50',
       'fileName': 'old1.mp3',
       'image':'pehlanasha.jpg'
    },
    {
        'name': 'Ek Sanam Chahiye',
        'artist': 'Kumar Sanu',
        'album': 'Ashiqui',
        'duration': '6:12',
        'fileName': 'old2.mp3',
        'image':'sanam.jpg'
    },
    {
        'name': 'Likhe Jo Khat Tujhe',
        'artist': 'Mohammad Rafi',
        'album': 'Kanyadaan',
        'duration': '4:32',
        'fileName': 'old3.mp3',
        'image':'khat.jpg'
    },
    {
        'name': 'Kisi Disco Mein Jayen',
        'artist': 'Udit Narayan, Alka Yagnik',
        'album': 'Chote Miyan Bade Miyan',
        'duration': '5:25',
        'fileName': 'old4.mp3',
        'image':'kisidisco.jpg'
    }]

var mashup= [{
        'name': 'Valentine Mashup 2017',
        'artist': 'Dj Shadow Dubai',
        'album': 'Desilicious 75',
        'duration': '5:06',
       'fileName': 'mashup1.mp3',
       'image':'valentine1.jpg'
    },
    {
        'name': 'The Love Mashup',
        'artist': 'Dj Kiran Kamath',
        'album': 'love Mashup 2016',
        'duration': '4:47',
        'fileName': 'mashup2.mp3',
        'image':'lovemashup.jpg'
    },
    {
        'name': 'Bollywood Love Mashup',
        'artist': 'Dj Alvee',
        'album': 'Mashups',
        'duration': '4:28',
        'fileName': 'Mashup3.mp3',
        'image':'bollywoodlove.jpg'
    },
    {
        'name': 'Zee Valentine Mashup',
        'artist': 'Dj Notorious',
        'album': 'Valentine Mashups',
        'duration': '3:47',
        'fileName': 'Mashup4.mp3',
        'image':'valentine2.jpg'
    }]

var party = [{
        'name': 'Chalti Hai Kya 9 se 12',
        'artist': 'Dev Nagi, Neha Kakkar',
        'album': 'Judwaa2',
        'duration': '4:22',
       'fileName': 'party1.mp3',
       'image':'9se12.jpg'
    },
    {
        'name': 'Disco Disco',
        'artist': 'Benny Dayal, Shirley Setia',
        'album': 'A Gentelman',
        'duration': '2:46',
        'fileName': 'party2.mp3',
        'image':'gentleman.jpg'
    },
    {
        'name': 'Ding Dang',
        'artist': 'Amit Mishra, Antra Mishra',
        'album': 'Munna Michael',
        'duration': '3:23',
        'fileName': 'party3.mp3',
        'image':'dingdang.jpg'
    },
    {
        'name': 'Oonchi Hai Building 2.0',
        'artist': 'Anu Malik, Neha Kakkar',
        'album': 'Judwaa2',
        'duration': '3:25',
        'fileName': 'party4.mp3',
        'image':'Building.jpg'
    }]


//initially set every mood false


var mood1clicked=false;
var mood2clicked=false;
var mood3clicked=false;
var mood4clicked=false;
var mood5clicked=false;
var mood6clicked=false;

function details(obj){
    var name="#song"+(i+1);
    var song=$(name);
    song.find('.song-name').text(obj.name);
    song.find('.song-artist').text(obj.artist);
       song.find('.song-album').text(obj.album); 
        song.find('.song-length').text(obj.duration);
     addSongNameClickEvent(obj,i+1);
    
}

/*
function allMoods(){
    $('.boximg').click(function(event) {
    var clickedmood = $(event.target);
        if(clickedmood.hasClass("rclass")==true){
            moodDetails(romantic);               // passes object type
        }  
        if(clickedmood.hasClass("eclass")==true){
             moodDetails(english);   
        }
        if(clickedmood.hasClass("iclass")==true){
             moodDetails(indopop);
        }
        if(clickedmood.hasClass("oclass")==true){
              moodDetails(oldgold); 
        }
        
        if(clickedmood.hasClass("mclass")==true){
              moodDetails(mashup);   
        }
        if(clickedmood.hasClass("pclass")==true){
             moodDetails(party);   
        }
    });   
}
*/

//new code for mood details

function allMoods(){
    $('.boximg').click(function(event) {
    var clickedmood = $(event.target).attr('name'); //string type
        moodDetails(clickedmood);
    });   
   
}



function moodDetails(moodName){
    console.log(typeof(moodName));
     $('#audioElement').attr('src',moodName[0].fileName);
            for(i=0;i<moodName.length;i++){
            var obj=moodName[i];
                details(obj);
            changeCurrentSongDetails(moodName[0]);
            } 
    
}
//loads song details of mood1
/*
$('.mood1').click(function () {
    mood1clicked = true; //mood1 clicked and gets true
    if(mood1clicked==true) {
    $('#audioElement').attr('src',romantic[0].fileName);
    for(i=0;i<romantic.length;i++){
    var obj=romantic[i];
details(obj);
    changeCurrentSongDetails(romantic[0]);
}
} 
});

//loads song details of mood2

$('.mood2').click(function () {
    mood2clicked = true;
    if(mood2clicked==true){
    $('#audioElement').attr('src',english[0].fileName);
    for(i=0;i<english.length;i++){
    var obj=english[i];
details(obj);
    changeCurrentSongDetails(english[0]);   
}
}
});

//loads song details of mood3


$('.mood3').click(function () {
    mood2clicked = true;
    if(mood2clicked==true){
        $('#audioElement').attr('src',indopop[0].fileName);
    for(i=0;i<indopop.length;i++){
    var obj=indopop[i];
details(obj);
        changeCurrentSongDetails(indopop[0]);
}
}
});

//loads song details of mood4

$('.mood4').click(function () {
    mood2clicked = true;
    if(mood2clicked==true){
        $('#audioElement').attr('src',oldgold[0].fileName);
    for(i=0;i<oldgold.length;i++){
    var obj=oldgold[i];
details(obj);
         changeCurrentSongDetails(oldgold[0]);
}
}
});

//loads song details of mood5

$('.mood5').click(function () {
    mood2clicked = true;
    if(mood2clicked==true){
        $('#audioElement').attr('src',mashup[0].fileName);
    for(i=0;i<mashup.length;i++){
    var obj=mashup[i];
details(obj);
    changeCurrentSongDetails(mashup[0]);
}
}
});


//loads song details of mood6

$('.mood6').click(function () {
    mood2clicked = true;
    if(mood2clicked==true){
        $('#audioElement').attr('src',party[0].fileName);
    for(i=0;i<party.length;i++){
    var obj=party[i];
details(obj);
          changeCurrentSongDetails(party[0]);
}
}
});
*/

//search function (same as datatbles)

function searchFunction() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}

//sets song duration on wondows loading

window.onload=function(){
    songduration();
    setInterval(function(){
        songduration();
    },1000);
    /*$('#myTable').DataTable({
        paging:false
    });*/
}


//toggles song on clicking on other or current song

function addSongNameClickEvent(songObj,position){
    var songName = songObj.fileName; 
    var id="#song"+position;
$(id).click(function() {
  var audio = document.querySelector('audio');
  var currentSong = audio.src;
  if(currentSong.search(songName) != -1)       //searches filename of song in the src
  {
    toggleSong();
  }
  else {
    audio.src = songName;
    toggleSong();
    changeCurrentSongDetails(songObj); 
  }
});
}

function changeCurrentSongDetails(songObj) {
    $('.current-song-image').attr('src','img/' + songObj.image)
    $('.current-song').text(songObj.name)
    $('.current-album').text(songObj.album)
}








function moodLoad2(){
    $('#mood').addClass('hidden');
    $('#player-list').removeClass('hidden');
    $('#piano').removeClass('hidden');
    $('#drum').removeClass('hidden');
    $('#search').removeClass('hidden');
    listenPlayPause();
}

// long song details according to mood

function romanticMood(){
    moodLoad2();
  $('#audioElement').attr('src',romantic[0].fileName);
    for(i=0;i<romantic.length;i++){
    var obj=romantic[i];
details(obj);
    changeCurrentSongDetails(romantic[0]);
}
}   
// long song details according to mood
 function englishMood(){
    moodLoad2();
  $('#audioElement').attr('src',english[0].fileName);
    for(i=0;i<english.length;i++){
    var obj=english[i];
details(obj);
    changeCurrentSongDetails(english[0]);
}
}  
// long song details according to mood
function indopopMood(){
    moodLoad2();
  $('#audioElement').attr('src',indopop[0].fileName);
    for(i=0;i<indopop.length;i++){
    var obj=indopop[i];
details(obj);
    changeCurrentSongDetails(indopop[0]);
}
}  
// long song details according to mood
function oldgoldMood(){
    moodLoad2();
  $('#audioElement').attr('src',oldgold[0].fileName);
    for(i=0;i<oldgold.length;i++){
    var obj=oldgold[i];
details(obj);
    changeCurrentSongDetails(oldgold[0]);
}
} 

// long song details according to mood
function mashupMood(){
    moodLoad2();
  $('#audioElement').attr('src',mashup[0].fileName);
    for(i=0;i<mashup.length;i++){
    var obj=mashup[i];
details(obj);
    changeCurrentSongDetails(mashup[0]);
}
}  

// long song details according to mood
function partyMood(){
    moodLoad2();
  $('#audioElement').attr('src',party[0].fileName);
    for(i=0;i<party.length;i++){
    var obj=party[i];
details(obj);
    changeCurrentSongDetails(party[0]);
}
}  



//ajax req for checking the users mood 



function moodAjax(convertedText){
                $.ajax({
  url: 'https://api.wit.ai/message',
  data: {
    'q': convertedText,
    'access_token' : 'QW5T3QZR46XQKLKJKCXSDWG6MESMYSIO'
  },
  dataType: 'jsonp',
  method: 'GET',
  success: function(response) {
      console.log("success!", response);
      if((response.entities.search_query[0].value == 'romantic')||(response.entities.search_query[0].value == 'romantic song')) {
        // Change current song to first song
        romanticMood() ;
      }
      else if(response.entities.search_query[0].value == 'english song') {
        englishMood() ;
      }
      else if(response.entities.search_query[0].value == 'indopop song') {
        indopopMood() ;
      }
      else if(response.entities.search_query[0].value == 'old song') {
        oldgoldMood() ;
      }
      else if(response.entities.search_query[0].value == 'mashup song') {
        mashupMood() ;
      }
      else if(response.entities.search_query[0].value == 'party song') {
        partyMood() ;
      }
  }
});
}

//records users voice for mood analysis

function moodRecord(){
    speechRs.rec_start('en-IN',function(final_transcript){
           var convertedText=final_transcript.toLowerCase();
           if (convertedText.length >0){
               speechRs.rec_stop();     //stop the recording
               console.log(convertedText);
        //mood ajax function called 
             moodAjax(convertedText);
           }
       }) ;
}






//ajax req for play pause and vol up down

    function listenPlayPause(){
        speechRs.rec_start('en-IN',function(final_transcript ){
           
           var convertedText=final_transcript.toLowerCase();
           if (convertedText.length >0){
                 speechRs.rec_stop();
               console.log(convertedText);
               // calls request play pause for send user  voice text
               requestPlayPause(convertedText);
               
           }
       }) ;
    
    }
    

//sends data to wit.ai and checks response
    function requestPlayPause(convertedText){
        $.ajax({
                url: 'https://api.wit.ai/message',
                data: {
                'q': convertedText,
                'access_token' : 'QW5T3QZR46XQKLKJKCXSDWG6MESMYSIO'
                },
                dataType: 'jsonp',
                method: 'GET',
                success: function(response) {
                    console.log("success!", response);
                    if(response.entities.intent[0].value == 'play') {
                        // Change current song to first song
                        toggleSong() ;
                    }
                    else if (response.entities.intent[0].value == 'pause') {
                        toggleSong() ;
                    }
                    else if(response.entities.intent[0].value == 'increase'){
                            increaseVolume();
                     }
                    else if(response.entities.intent[0].value == 'decrease'){
                            decreaseVolume();
                     }
                }
               });
        
        //again triggers listening after performing the action
        
        
        listenPlayPause();
    }
    
//function for increaing volume

function increaseVolume(){
    document.getElementById('audioElement').volume+=0.5;
    $('[data-toggle="popoverIncrease"]').popover();   
    console.log("increased by 0.5");
}


//function for decreaing volume


function decreaseVolume(){
    document.getElementById('audioElement').volume-=0.5;
    $('[data-toggle="popoverDecrease"]').popover();   
    console.log("decreased by 0.5");
}