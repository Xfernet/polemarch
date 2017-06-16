
function pmItems()
{ 
    this.pageSize = 2; 
    this.model = {}
    this.model.selectedItems = {}
    
    this.toggleSelect = function(item_id)
    {
        this.model.selectedItems[item_id] = !this.model.selectedItems[item_id]

        var count = 0;
        for(var i in this.model.selectedItems)
        {
            if(this.model.selectedItems[i])
            {
                count += 1
            }
        }

        this.model.selectedCount = count;
        return this.model.selectedItems[item_id];
    }
    
    this.validateHostName = function(name)
    {
        if(!name)
        {
            return false; 
        }
        
        var regexp = {
            ipTest : /^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$/,
            ip6Test : /((^|:)([0-9a-fA-F]{0,4})){1,8}$/,
            domenTest : /^((\.{0,1}[a-z0-9][a-z0-9-]{0,62}[a-z0-9]\.{0,1})*)$/
        }

        if(regexp.ipTest.test(name))
        {
            return true;
        }

        if(regexp.ip6Test.test(name))
        {
            return true;
        }

        if(regexp.domenTest.test(name))
        {
            return true;
        }

        return false; 
    }

    this.validateRangeName = function(name)
    {
        if(!name)
        {
            return false; 
        }
        
        return name.replace(/\[([0-9A-z]+):([0-9A-z]+)\]/g, "$1") && name.replace(/\[([0-9A-z]+):([0-9A-z]+)\]/g, "$2")
    }
    
    this.showList = function(holder, menuInfo, data){}

    this.showItem = function(holder, menuInfo, data){}
 
    this.showNewItemPage = function(holder, menuInfo, data){}
 
    /**
     * Обновляет поле модел polemarch.model.hostslist и ложит туда список пользователей
     * Обновляет поле модел polemarch.model.hosts и ложит туда список инфу о пользователях по их id
     */
    this.loadItems = function(){}
 
    /**
     * Обновляет поле модел polemarch.model.hosts[item_id] и ложит туда пользователя
     */
    this.loadItem = function(item_id){}
 
    /**
     * @return $.Deferred
     */
    this.addItem = function(){}
 
    /**
     * @return $.Deferred
     */
    this.updateItem = function(item_id){}
  
    /**
     * @return $.Deferred
     */
    this.deleteItem = function(item_id){}
 
    this.jsonEditor = function(json)
    { 
        return spajs.just.render('jsonEditor', {data:json})
    }

    this.jsonEditorGetValues = function()
    { 
        var data = {}
        var arr = $(".jsonEditor-data")
        for(var i = 0; i< arr.length; i++)
        {
            var index = $(arr[i]).attr('data-json-name') 
            data[index] = $(arr[i]).val()
        }

        return data
    }

    this.jsonEditorAddVar = function(name, value)
    {
        var name = $('#new_json_name').val()
        var value = $('#new_json_value').val()

        if(!name)
        {
            $.notify("Empty varible name", "error");
            return;
        }
        
        if($("#json_"+name+"_value").length)
        {
            $.notify("This var already exists", "error");
            return;
        }

        $('#new_json_name').val('')
        $('#new_json_value').val('')

        $("#jsonEditorVarList").append(spajs.just.render('jsonEditorLine', {name:name, value:value}))
    }

    ////////////////////////////////////////////////
    // pagination
    ////////////////////////////////////////////////

    this.paginationHtml = function(list)
    {
        var totalPage = list.count / list.limit
        if(totalPage > Math.floor(totalPage))
        {
            totalPage = Math.floor(totalPage) + 1
        }

        var currentPage = 0;
        if(list.offset)
        {
            currentPage = Math.floor(list.offset / list.limit)
        }
        var url = window.location.href  
        return  spajs.just.render('pagination', {
            totalPage:totalPage,
            currentPage:currentPage,
            url:url})
    }

    this.getTotalPages = function(list)
    {
        var totalPage = list.count / list.limit 
        return  totalPage
    }
}


/**
 * Тестовый тест, чтоб было видно что тесты вообще хоть как то работают.
 */
function trim(s)
{
    if(s) return s.replace(/^ */g, "").replace(/ *$/g, "")
    return '';
}

