<%inherit file="base.mako" />

<%block name="content">
<div class="hero-unit">
    <h1>Hello DneprPy!</h1>
</div>

<li><a href="${request.route_url('addpost')}">Add new post</a></li>


<div class="poststream">
%for post in posts:
<div class="media" data-id="${post.id}">
  %if post.image:
  <a class="pull-left" href="#">
    <img class="media-object img-polaroid" src="${post.get_thumb()}">
  </a>
  %endif
  <div class="media-body">
    <h4 class="media-heading">${post.title}</h4>
    <p>
        ${post.text}
    </p>

##    %if post.user:
##        <p>
##            <b>Author:</b> ${post.user.login}
##        </p>
##    %endif

  </div>
</div>

%endfor

</div>


</%block>
