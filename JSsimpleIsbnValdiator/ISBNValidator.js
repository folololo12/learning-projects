function isValidIsbn10(str) {
 let d = str.length
 let div = 0
 let itt = 0
 for(let i = 0; i< d; i++ ){
    if (str[i] === '-') {
      continue
    }
   if (!isNaN(Number(str[i]))){
     itt++
     let num = parseInt(str[i])
     div = div + num * itt
   }
   
    else if(str[i] === "X"){
      itt++
      if(itt === 10){
        div += 10 * itt;

      } else{
        return false
      }
   }
   else{
     return false
   }
 }
 if(div % 11 === 0){
  return true;
 }
 else{
   return false
 }
}