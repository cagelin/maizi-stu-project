$(function(){
  $(document).on('click', function() {   
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideUp();
    //清除搜索结果
    $('#search-CareerCourse').html('');
    $('#search-Course').html('');
    $('.show-card').removeClass('slideInDown').addClass('hidden');
  });
  
  //弹出框显示后的一些操作
  $('.modal').on({
    'show.bs.modal': function (e) {
      $(this).children('.modal-dialog')
      .css('margin','0 auto')
      .wrap('<div class="wrap-modal-main"></div>')
      .wrap('<div class="wrap-modal-con"></div>');
      $('.wrap-modal-main').css({
        'display': 'table',
        'width': '100%',
        'height': '100%'
      });
      $('.wrap-modal-con').css({
        'display': 'table-cell',
        'width': '100%',
        'vertical-align': 'middle'
      });

    },
    'shown.bs.modal': function (e) {
      $(this).find('.form-control').first().focus();
    }
  });
  
  //登陆
  $('#btnLogin').on('click', function () {
    $('#registerModal').modal('hide');
  });
  $('.show-card').on('click', function (event) {
    event.stopPropagation();
  });
  $('.dt-username').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    $('.show-card').toggleClass('hidden slideInDown');
  });

  //忘记密码
  $('#btnForgetpsw').on('click', function () {
    $('#loginModal').modal('hide');
  });

  //注册
  $('#btnRegister').on('click', function () {
    $('#loginModal').modal('hide');
  });

  //创建班级
  
  //search
  $('#search').on({
    click: function(event) {
      event.stopPropagation();
    },
    focus: function() {
      if($(this).val() == '') {
        $('#hotkeyword').slideDown();
      }
    },

    // ajax 搜索
    keyup:function() {
      $('#hotkeyword').slideUp();
      var word = $('#search').val();
      var ccl_str='';
      // var ccl_str_t='';
      var cl_str='';
      // var cl_str_t='';
      if(word!=''){
        $.ajax({url:"/keyword_search",
              type:"get",
              data: {"word":word},
              dataType: "json",
              error:function () {
                $('#search-CareerCourse').html('搜索出错');
                $('#search-Course').html('搜索出错');
                // $('#search-CareerCourse_t').html('搜索出错');
                // $('#search-Course_t').html('搜索出错');
              },
              success: function (data) {
                if ("career_course_lists"in data&&data["career_course_lists"].length>0){
                $.each(data["career_course_lists"],function (k, v) {
                  ccl_str+= '<a href="'+v["market_page_url"]+'" style="background-color:'+v["color"]+'">'+v["name"]+'</a>';
                  // ccl_str_t+='<div><span style="background-color:'+v["color"]+'"><img src="images/course/android.png"></span><a href="'+v["market_page_url"]+'">'+v["name"]+'</a></div>'
              });
                $('#search-CareerCourse').html(ccl_str);
                // $('#search-CareerCourse_t').html(ccl_str_t);
                }else {
                   $('#search-CareerCourse').html('没有相关职业课程');
                }
                if("course_lists"in data&&data["course_lists"].length>0){
                $.each(data["course_lists"],function (k, v) {
                  cl_str+= '<a href="'+v["market_page_url"]+'" style="background-color:'+v["color"]+'">'+v["name"]+'</a>'
                  // cl_str_t+='<div><span style="background-color:'+v["color"]+'"><img src="images/course/android.png"></span><a href="'+v["market_page_url"]+'">'+v["name"]+'</a></div>'
              });
                $('#search-Course').html(cl_str);
                  // $('#search-Course_t').html(cl_str_t);
                }else {
                   $('#search-Course').html('没有相关课程');
                }
                $('#keyword-group').slideDown();
              }
      })}
    }
    // ajax结束
  });
  $('.search-dp').click(function(event) {
    event.stopPropagation();
  });
  $('#hotkeyword a').click(function(event) {
    event.preventDefault();
    $('#search').val($(this).text());
    // 触发keyup事件
     $('#search').trigger("keyup");
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideDown();

  });


  //点击收藏
  $('.house').on('click', function (event) {
    event.preventDefault();
    var _thisI = $(this).children('i');
    var _thisIclass = _thisI.hasClass('v5-icon-saved');
    _thisI.toggleClass('v5-icon-saved');
    var _text = (_thisIclass == true) ? '收藏' : '已收藏';
    $(this).children('span').text(_text);
  });
  
  $('.plan-tip').hover(function() {
    $('.plan-tip-box').addClass('show');
  }, function() {
    $('.plan-tip-box').removeClass('show');
  });
  
  $('.feedback-switch').click(function(){
    $(this).toggleClass('active');
    var _has_active = $(this).hasClass('active');
    if(_has_active){
      $(this).parent('.feedback').animate({
        bottom:0
      },500);
    }
    else{
      $(this).parent('.feedback').animate({
        bottom:'-300px'
      },500);
    }
  });
  
  $('img#viptips').hover(function(){
    $(this).tooltip({
      template: '<div class="tooltip tooltip-vip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
    });
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('[data-toggle="tooltip"]').hover(function(){
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('.class-list li').click(function(){
    event.preventDefault();
    $(this).toggleClass('active');
    if($(this).hasClass('active')){
      $(this).siblings().removeClass('active');
      $('#btn-okpay').removeClass('btn-micv5-disabled1').removeAttr('disabled');
    }
    else{
      $('#btn-okpay').addClass('btn-micv5-disabled1').attr('disabled','disabled');
    }
  })
});

function v5_popover_tpl(tpl_class,elem,popover_container,popover_placement,popover_trigger){
  var elem_popover = document.getElementById(elem);
  var popover_c = $('.' + popover_container);
  popover_c.popover({
    content:elem_popover,
    container:'body',
    template:'<div class="popover ' + tpl_class + '" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>',
    placement:popover_placement,
    trigger:popover_trigger,
    html: true
  });
}

// 首页课程ajax请求
function get_course(index, course_order_by) {
  var course_lists = $("#" + course_order_by + " .course-list-index");
  var page_list = $("#" + course_order_by + " .fr");
    course_lists.empty();
    $.ajax({
        url:"/course_search",
        type:"get",
        async:false,
        data:{'index':index,
            'course_order_by':course_order_by},
        dataType:"json",
        error:function () {
          course_lists.html("获取课程出错");
          page_list.html("");
        },
        success: function (data) {
          //解析数据
          if("error"in data&&data["error"].length>0){
            course_lists.html(data["error"]);
            page_list.html("");
          }else {
          $.each(data['result'],function (k,v) {

            var li = '<li class="col-xs-12 col-sm-6 col-md-6 col-lg-3"><a href="' + v[0] + '">' +
                                    '<dl><dt><div><img src="uploads/' + v[1] + '"></div>' +
                                    '</dt> <dd><span>' + v[2] + '</span><p>' + v[3] + '人正在学习</p>' +
                                    '</dd> </dl> </a></li>';
            course_lists.append(li);

          });
          page_list.html('');
          if(data['current_page']>1){
            page_list.append('<li><a href="javascripts:void(0)" class="v5-icon v5-icon-prev" onclick="get_course(' + (data["current_page"] - 1) +
                                    ',\'' + course_order_by + '\');"></a></li>');
          }
          for(var i=0; i< data['total_pages'];i++) {
            if (data['current_page'] == i + 1) {
              page_list.append('<li><a href="javascripts:void(0)" class="page-num active" onclick="get_course(' + (i + 1) + ',\'' + course_order_by + '\');">' + (i + 1) + '</a></li>')
            } else {
              page_list.append('<li><a href="javascripts:void(0)" class="page-num" onclick="get_course(' + (i + 1) + ',\'' + course_order_by + '\')">' + (i + 1) + '</a></li>')
            }
          }
          if(data['current_page']!=data['total_pages']){
            page_list.append('<li><a href="javascripts:void(0)" class="v5-icon v5-icon-next" onclick="get_course(' + (data["current_page"] + 1) +
                                    ',\'' + course_order_by + '\');"></a></li>');
          }
        }
        }
    })
}
get_course(1,'new');
get_course(1,'most');
get_course(1,'hot');