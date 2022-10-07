// The first time the page loads, get info from the only existing main tag
try{
  spa_title = document.querySelector("main").dataset.spa_title || ''
  spa_url = document.querySelector("main").dataset.spa_url || '/'
  current_url = spa_url
  spa_hide = document.querySelector("main").dataset.spa_hide
  spa_show = document.querySelector("main").dataset.spa_show
  spa_display = document.querySelector("main").dataset.spa_display || "block"
  spa_set_active_class = document.querySelector("main").dataset.spa_set_active_class || "/"
  // console.log(spa_url, spa_hide, spa_show, spa_display)
  document.title = spa_title
  // Set the state for the first loaded page
  history.replaceState({"spa_url":spa_url}, '', spa_url)
}catch(ex){
  console.log("spa error: data is missing in the main tag")
  console.log(ex)
}

// ##############################
// async function spa(url, hide, show, title, replace_state = true){
async function spa(spa_url, replace_state = true){
  
  // If the user cliks on the link to show the same page again
  // spa_url = replace_state ? event.target.getAttribute("href") : spa_url
  spa_url = replace_state ? event.currentTarget.getAttribute("href") : spa_url
  if( current_url == spa_url ){ return }

  current_url = spa_url
  console.log('current_url', current_url);
  console.log('spa_url', spa_url);  
  // console.log("spa_url", spa_url)

  // Check if page is already loaded
  if( ! document.querySelector(`[data-spa_url="${spa_url}"]`) ){
    // console.log("loading spa...")
    // console.log("loading url...", spa_url)
    // Load the page
    let conn = await fetch(spa_url, { headers : {"spa":"yes"} })
    let html = await conn.text()
    // console.log(html)
    document.querySelector("body > nav").insertAdjacentHTML("afterend", html)
  }
  try{
    // The loaded main element is in the DOM, extract instructions from the data- attributes
    // console.log(`[data-spa_url="${spa_url}"]`)
    main_element = document.querySelector(`[data-spa_url="${spa_url}"]`)
    // On page not found
    if( ! main_element){
      main_element = document.querySelector(`[data-spa_url="404"]`)
    }
    console.log("main_element", main_element)
    // spa_title = main_element.dataset.spa_title
    spa_title = main_element.getAttribute("data-spa_title")
    console.log("title", spa_title)
    spa_hide = main_element.dataset.spa_hide
    spa_show = main_element.dataset.spa_show
    spa_display = main_element.dataset.spa_display || "block"
    spa_mode = main_element.dataset.spa_mode
    spa_set_active_class = main_element.dataset.spa_set_active_class
  }catch(ex){
    console.log("spa error: cannot select main_element")
  }

  // Hide spas
  try{ 
    document.querySelectorAll(spa_hide).forEach(elem=>{elem.style.display = "none"} )
  }catch(err){
    console.log(err)
  }
  // Show spa
  try{
    main_element.style.display = spa_display
    // document.querySelector(jArgs.show).style.display = jArgs.display }
  }catch(ex){
    // Show 404
    // document.querySelector("#spa_404").style.display = "grid"
  }
  // Set active class
  try{
    document.querySelectorAll(".active").forEach(elem=>{ elem.classList.remove("active") })
    console.log('spa_set_active_class', spa_set_active_class);
    document.querySelectorAll(spa_set_active_class).forEach(elem=>{ elem.classList.add("active") })
  }catch(ex){

  }  

  // document.title = jArgs.title
  
  document.title = spa_title
  if(replace_state){
    history.pushState({"spa_url":spa_url}, '', spa_url)
  }

}

// ##############################
window.addEventListener("popstate", event => {
  // spa(event.state.url, event.state.hide, event.state.show, event.state.title, false)
  spa(event.state.spa_url, false)
  return false
})

// ##############################















