/*
  This is a combined version of VeryIDE 
  Last Updated:: 2017/03/21 17:29:13.
  Files include::  /static/js/app.js
*/
(function (win, doc) {
    function SetHome(homes, url) {
        try {
            homes.style.behavior = 'url(#default#homepage)';
            homes.setHomePage(url);
        } catch (e) {
            if (window.netscape) {
                try {
                    netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
                } catch (e) {
                    alert("\u62b1\u6b49\uff0c\u6b64\u64cd\u4f5c\u88ab\u6d4f\u89c8\u5668\u62d2\u7edd\uff01\n\n\u8bf7\u5728\u6d4f\u89c8\u5668\u5730\u5740\u680f\u8f93\u5165\u201cabout:config\u201d\u5e76\u56de\u8f66\u7136\u540e\u5c06[signed.applets.codebase_principal_support]\u8bbe\u7f6e\u4e3a'true'");
                }
            } else {
                alert("\u62b1\u6b49\uff0c\u60a8\u6240\u4f7f\u7528\u7684\u6d4f\u89c8\u5668\u65e0\u6cd5\u5b8c\u6210\u6b64\u64cd\u4f5c\u3002\n\n\u60a8\u9700\u8981\u624b\u52a8\u5c06\u3010" + url + "\u3011\u8bbe\u7f6e\u4e3a\u9996\u9875\u3002");
            }
        }
    }

    function AddFavorite(title, url) {
        try {
            window.external.addFavorite(url, title);
        } catch (e) {
            try {
                window.sidebar.addPanel(title, url, "");
            } catch (e) {
                alert("\u62b1\u6b49\uff0c\u60a8\u6240\u4f7f\u7528\u7684\u6d4f\u89c8\u5668\u65e0\u6cd5\u5b8c\u6210\u6b64\u64cd\u4f5c\u3002\n\n\u52a0\u5165\u6536\u85cf\u5931\u8d25\uff0c\u8bf7\u4f7f\u7528Ctrl+D\u8fdb\u884c\u6dfb\u52a0");
            }
        }
    }

    R('a[rel=favorite]').bind('click', function () {
        AddFavorite(document.domain, location.href);
    });
    R('a[rel=sethome]').bind('click', function () {
        SetHome(this, document.domain);
    });
    R('form[name=filterForm]').bind('submit', function (idx, e) {
        R.Event(e).stop();
        var search = document.filterForm.action;
        var kw = R("input[name=kw]").value();
        var tk = R("input[name=token]").value();
        window.location.href = search + '?kw=' + kw + '&token=' + tk;
    });
    R.Lazy.init();
    R.Lazy.run();
    if (document.getElementById('D1pic1')) {
        Qfast(false, 'widgets', function () {
            K.tabs({
                id: 'fsD1',
                conId: "D1pic1",
                tabId: "D1fBt",
                tabTn: "a",
                conCn: '.fcon',
                auto: 1,
                effect: 'fade',
                eType: 'click',
                pageBt: true,
                bns: ['.prev', '.next'],
                interval: 3000
            })
        })
    }
})(window, document, undefined);