function bindEamailyanzhen(){
    $("#captcha-btn").click(function (event){
        var $this=$(this);

        event.preventDefault();

        var email=$("#exampleInputEmail1").val();
        $.ajax({
            url:"/user/mail/yanzhen?email="+email,
            method:"GET",
            success:function (result){
                console.log(result);
                var code=result['code'];
                if (code==200){
                    var countdown=10;
                    //开始倒计时之前，取消按钮的点击事件
                    $this.off("click");
                    var timer=setInterval(function (){
                        $this.text(countdown);
                        countdown-=1;
                        if(countdown<=0)
                        {
                            //清掉计时器
                            clearInterval(timer);
                            //恢复点击框文本
                            $this.text("获取验证码");
                            //重新绑定点击事件
                            bindEamailyanzhen();
                        }
                    },1000);

                    // alert('发送成功');
                }
                else{
                    alert(result['message']);
                }

            },
            fail:function (error)
            {
                console(error);
            }
        })

    }
    )
}


$(function (){

    bindEamailyanzhen();


});