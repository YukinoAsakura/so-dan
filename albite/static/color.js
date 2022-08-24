var cols=document.getElementsByClassName("article");
var i =0
for (var i=0;i< cols.length;i++) {
    if (i%3 ==0){
        cols[i].style.backgroundColor ='#ffffff'
    }
    else if(i%3 ==1){
        cols[i].style.backgroundColor ='#5abce2'
    }
    else if(i%3 ==2){
        cols[i].style.backgroundColor ='#ffd700'
    }
}