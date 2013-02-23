<html>
    <head>
        <link rel="stylesheet" href="${request.static_url('blogpy:static/css/bootstrap.css')}">
        <script src ="${request.static_url('blogpy:static/js/jquery.min.js')}"></script>
        <script src ="${request.static_url('blogpy:static/js/bootstrap.js')}"></script>
        <script src ="${request.static_url('blogpy:static/js/underscore-min.js')}"></script>
        <script src ="${request.static_url('blogpy:static/js/utilities.js')}"></script>
        <script>
##        var X_CSRF_TOKEN = '${csrf_token}';
        </script>
    </head>
    <body>
        <div class="container">
            <%block name="content" />
        </div>
    </body>
</html>
