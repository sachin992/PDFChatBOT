# css = '''
# <style>
# .chat-message {
#     padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
# }
# .chat-message.user {
#     background-color: #2b313e
# }
# .chat-message.bot {
#     background-color: #475063
# }
# .chat-message .avatar {
#   width: 20%;
# }
# .chat-message .avatar img {
#   max-width: 78px;
#   max-height: 78px;
#   border-radius: 50%;
#   object-fit: cover;
# }
# .chat-message .message {
#   width: 80%;
#   padding: 0 1.5rem;
#   color: #fff;
# }
# '''

# bot_template = '''
# <div class="chat-message bot">
#     <div class="avatar">
#         <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
#     </div>
#     <div class="message">{{MSG}}</div>
# </div>
# '''

# user_template = '''
# <div class="chat-message user">
#     <div class="avatar">
#         <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
#     </div>    
#     <div class="message">{{MSG}}</div>
# </div>
# '''



css = """
<style>
.chat-message {
    margin: 10px 0;
    display: flex;
    align-items: flex-start;
}

.chat-message.user {
    justify-content: flex-end;
}

.chat-message .message {
    max-width: 70%;
    padding: 12px 18px;
    border-radius: 12px;
    color: white;
    font-size: 16px;
    line-height: 1.4;
}

.chat-message.user .message {
    background: #005cfa;
    border-bottom-right-radius: 0;
}

.chat-message.bot .message {
    background: #2b313e;
    border-bottom-left-radius: 0;
}

.avatar img {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    margin-right: 10px;
}
</style>
"""

chat_container_css = """
<style>
.chat-box {
    height: 70vh;
    overflow-y: auto;
    padding: 10px 5px;
    background: #11141a;
    border-radius: 8px;
}
.input-bar {
    position: fixed;
    bottom: 0;
    left: 20%;
    width: 60%;
    background: #0e1117;
    padding: 12px;
    border-top: 1px solid #30363d;
}
.input-inner input {
    width: 100%;
    padding: 14px;
    font-size: 16px;
    border-radius: 8px;
}
</style>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar"><img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png"></div>
    <div class="message">{{MSG}}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
</div>
"""

scroll_script = """
<script>
    var chatBox = window.parent.document.querySelector('#chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
</script>
"""
