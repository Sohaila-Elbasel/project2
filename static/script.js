document.addEventListener('DOMContentLoaded', () => {

  //check if there is username
  if(!localStorage.getItem('user_name')){
    document.querySelector('.displayname-div').style.display = "flex";
    document.querySelector('.displaycontent-div').style.display = "none";
  }else{
    document.querySelector('.displayname-div').style.display = "none";
    document.querySelector('.displaycontent-div').style.display = "flex";
    document.querySelector('.create_channel_div').style.display = "none";
  }

  //enter username
  form = document.querySelector(".name-form");
  form.onsubmit = () => {
    name = document.querySelector('#displayName').value;
    if(!name.replace(/\s/g, '').length){
      document.querySelector('.form-group small').style.display = "flex";
      return false;
    }
    localStorage.setItem('user_name', name);
  };

  //display page elements
  document.querySelector(".hi_name").innerHTML = "HI, " + localStorage.getItem('user_name');
  channels_links();

  // create channel
  document.querySelector('.create_channel').onclick = () => {
    document.querySelector('.channel_content').style.display = "none";
    document.querySelector('.create_channel_div').style.display = "flex";
  }

  //display messages function
  function displayMessages(messages){
    document.querySelector('.list-group').innerHTML = '';
    if (messages){
      for (index in messages){
        //main div
        div_main = document.createElement('div');
        div_main.className = 'list-group-item border-bottom';

        //info div insid main div
        div_info = document.createElement('div');
        div_info.className = 'd-flex w-100 justify-content-between';
        //inside info div
        h6 = document.createElement('h6');
        h6.className = 'mb-1';
        h6.style.color = '#d95284';
        h6.innerHTML = messages[index]['username'];

        small = document.createElement('small');
        small.innerHTML = messages[index]['date'];

        //p and small inside main div
        p= document.createElement('p');
        p.className = 'mb-1';
        p.innerHTML = messages[index]['text'];

        small2 = document.createElement('small');
        small2.innerHTML = 'This is small';

        // append elements
        div_info.append(h6);
        div_info.append(small);
        div_main.append(div_info);
        div_main.append(p);
        div_main.append(small2);

        document.querySelector('.list-group').append(div_main);

      }
    }
  }

  //display channel function
  function display_channel(name){
    document.querySelector('.displayname-div').style.display = "none";
    content = document.querySelector('.displaycontent-div');
    content.style.display = "flex";
    document.querySelector('.channel_content').style.display = "flex";
    document.querySelector('.create_channel_div').style.display = "none";
    fetch(`/display/${name}`)
    .then(response => response.json())
    .then(data => {
      displayMessages(data['messages']);
    })
    .catch(error => {
      console.log(error);
    });
  }

  //submit new channel
  document.querySelector('.channel-form').onsubmit = () => {
    name = document.querySelector('#channel_name').value;
    fetch(`/create/${name}`)
    .then(response => {
      var a = document.createElement('a');
      var link = document.createTextNode(name);
      a.href = '#';
      a.appendChild(link);
      var li = document.createElement('li');
      li.innerHTML = '- ';
      li.appendChild(a);
      document.querySelector('.left ul').appendChild(li);
      display_channel(name);
    })
    .catch(error => {
      console.log(`${error}`);
    });
    return false;
  }

  //channels links function
  function channels_links(){
    document.querySelectorAll('aside ul li a').forEach(link => {
      link.onclick = function(){
        display_channel(this.text);
        console.log(this.text);
      }
    });

  }
});
