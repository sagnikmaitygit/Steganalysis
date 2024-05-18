function readURL(input) {
    console.log("Souvik s great")
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}


function submitEncode(input){
    event.preventDefault();
    var pass=$('#key').val();
    var text=$('#text').val();
    var image=$('#file').val();
    if(pass=="" || text=="" || image==""){
        alert("Please Fill The Form Corectly");
    }else{
        if(pass.length!=8){
            alert("Please Make Sure Password Is 8 Character Long")
        }else{
            $("#encodeForm").submit();
        }
    }
}

function submitDecode(input){
    event.preventDefault();
    var pass=$('#key').val();
    var image=$('#file').val();
    if(pass=="" || image==""){
        alert("Please Fill The Form Corectly");
    }else{
        if(pass.length!=8){
            alert("Please Make Sure Password Is 8 Character Long")
        }else{
            $("#decodeForm").submit();
        }
    }
}


function myFunction() {
    var copyText = document.getElementById("decode_output");
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    alert("Copy Successfully:"+copyText.value)
    document.execCommand("copy");
    
}