


function hide_show_menu(){         
    console.log("button clicked")
    document.getElementById('showMenu').classList.toggle('hidden')
}



function Algebric_lessons(){
  hide_show_inner('1', 'A')
  console.log("Algebric")
}


function Next_lessons(){
  hide_show_inner('2', 'B')
  console.log("next lesson")
}





/*moving to lesson-level*/
function lesson_level_1(){
  hide_show_menu()
  hide_show_lesson_levels_category('option')
  
}




function toggle_examples(){
  show_div('examples')
  /*hide_show_lesson_levels_category('example')*/
}




function toggle_practice(){
  hide_div('examples')
  show_div('practice')
  /*hide_show_lesson_levels_category('practice')*/
}









/*functions to hide or show inner menu*/
function hide_show_inner(caret_id,inner_id){
  document.getElementById(caret_id).classList.toggle('rotate')
  document.getElementById(inner_id).classList.toggle('show')
  
}


/*function to hide or show lesson levels category*/
function hide_show_lesson_levels_category(div_id){
  document.getElementById(div_id).classList.toggle('hidden')
}


/*function to toggle nav bar*/
function toggle_nav_bar(nav_id){
  document.getElementById(nav_id).classList.toggle('hidden')
}



/*function to hide div*/
function hide_div(div_id){
  document.getElementById(div_id).classList.add('hidden')
}


/*funtion to show div*/
function show_div(div_id){
document.getElementById(div_id).classList.remove('hidden')
}


/*function to rotate caret*/
function rotate_caret(caret_id){
  document.getElementById(caret_id).classList.toggle('rotate')
}





function hide_show_xl_menu(){         
  console.log("button clicked")
  toggle_nav_bar('xl-nav')
  
}


function xl_Assumptions(){
  toggle_nav_bar('xl-nav')
  toggle_nav_bar("assumptions")
  rotate_caret('1')  
}


function useful_operations(){
  toggle_nav_bar("operations")
  rotate_caret('2')  
}