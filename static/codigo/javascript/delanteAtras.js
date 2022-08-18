function ODSatras(){
  if(document.getElementById("2img").hidden==false){
    document.getElementById("2img").hidden = true
    document.getElementById("7img").hidden = false
    document.getElementById("2txt").hidden = true
    document.getElementById("7txt").hidden = false
        
  } else if (document.getElementById("5img").hidden==false){
    document.getElementById("5img").hidden = true
    document.getElementById("2img").hidden = false 
    document.getElementById("5txt").hidden = true
    document.getElementById("2txt").hidden = false 
        
  } else if (document.getElementById("7img").hidden==false){
    document.getElementById("7img").hidden = true
    document.getElementById("5img").hidden = false 
    document.getElementById("7txt").hidden = true
    document.getElementById("5txt").hidden = false 
  }
}

function ODSdelante() {
  if(document.getElementById("2img").hidden==false){
    document.getElementById("2img").hidden = true
    document.getElementById("5img").hidden = false
    document.getElementById("2txt").hidden = true
    document.getElementById("5txt").hidden = false
        
  } else if (document.getElementById("5img").hidden==false){
    document.getElementById("5img").hidden = true
    document.getElementById("7img").hidden = false 
    document.getElementById("5txt").hidden = true
    document.getElementById("7txt").hidden = false 
        
  } else if (document.getElementById("7img").hidden==false){
    document.getElementById("7img").hidden = true
    document.getElementById("2img").hidden = false 
    document.getElementById("7txt").hidden = true
    document.getElementById("2txt").hidden = false 
  }
}