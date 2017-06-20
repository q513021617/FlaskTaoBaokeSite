(function(win,doc){
        var s = doc.createElement("script"), h = doc.getElementsByTagName("head")[0];
        if (!win.alimamatk_show) {
            s.charset = 'gbk';
            s.async = true;
            s.src = "http://a.alimama.cn/tkapi.js";
            s.kslite = "";
            h.insertBefore(s, h.firstChild);
        }
        var o = {
            pid: "22398476",
            unid:"",
            appkey:"23702051",
            plugins: [
                {name: 'keyword'},   /*内文关键字插件*/
                {name: 'aroundbox'}  /*任意位置角标插件*/
            ]
        }
        win.alimamatk_onload = win.alimamatk_onload || [];
        win.alimamatk_onload.push(o);
    })(window,document);