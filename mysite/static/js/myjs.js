	var langTools = ace.require("ace/ext/language_tools");
	var editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.getSession().setMode("ace/mode/java");
	
	editor.setOptions({
			enableBasicAutocompletion : true,
			enableLiveAutocompletion : true
		});
		// uses http://rhymebrain.com/api.html
	editor.commands.on("afterExec", function(e) {
			if (e.command.name == "insertstring" && /^[\\.\(.]$/.test(e.args)) {
				editor.execCommand("startAutocomplete");
			}
		});
	var rhymeCompleter = {
			getCompletions : function(editor, session, pos, prefix, callback) {
				/* if (prefix.length === 0) { callback(null, []); return } */
				console.log("prefix" + prefix);
				/* $.getJSON(
				    "http://rhymebrain.com/talk?function=getRhymes&word=" + prefix,
				    function(wordList) {
				        // wordList like [{"word":"flow","freq":24,"score":300,"flags":"bc","syllables":"1"}]
				        callback(null, wordList.map(function(ea) {
				            return {name: ea.word, value: ea.word, score: ea.score, meta: "rhyme"}
				        }));
				    }) */
				$.getJSON("loadCodeNote.action?filePath="
						+ $("#input-projectpath").val() + "/"
						+ $("#input-filename").val() + ".java", function(
						wordList) {
					console.log("@@@@@" + wordList);
					// wordList like [{"word":"flow","freq":24,"score":300,"flags":"bc","syllables":"1"}]
					callback(null, wordList.map(function(ea) {
						return {
							name : ea.word,
							value : ea.word,
							score : ea.score,
							meta : "rhyme"
						}
					}));
				})
			}
		}
	langTools.addCompleter(rhymeCompleter);
	
	
	
	
	
	
$(document).ready(function(){
	
	$(".subbox>a").click(function(){
		if($(this).hasClass("cur")){
			return;
			}else{
				var theIndex=$(this).index();
				$(".subbox>a").removeClass();
				$(this).addClass("cur");
				$(".mainbox").children().hide().eq(theIndex).show();
				
				
				}
		
		
		
		});
	
	
	});
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	