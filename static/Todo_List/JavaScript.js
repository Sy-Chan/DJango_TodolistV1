function check(checkbox){
  if(checkbox.checked){
    document.getElementsByClassName("checkButt")[0].disabled = false;
    document.getElementsByClassName("checkButt")[1].disabled = false;

  }else{
    document.getElementsByClassName("checkButt")[0].disabled = true;
    document.getElementsByClassName("checkButt")[1].disabled = true;
  }
}
