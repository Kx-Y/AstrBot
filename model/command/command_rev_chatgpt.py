from model.command.command import Command
from model.provider.provider_rev_chatgpt import ProviderRevChatGPT

class CommandRevChatGPT(Command):
    def __init__(self, provider: ProviderRevChatGPT):
        self.provider = provider
        
    def check_command(self, message: str, role, platform: str):
        hit, res = super().check_command(message, role, platform)
        if hit:
            return True, res
        if self.command_start_with(message, "help", "帮助"):
            return True, self.help()
        elif self.command_start_with(message, "reset"):
            return True, self.reset()
        elif self.command_start_with(message, "update"):
            return True, self.update(message, role)
        elif self.command_start_with(message, "keyword"):
            return True, self.keyword(message, role)
        return False, None
    
    def reset(self):
        return False, "此功能暂未开放", "reset"
    
    def help(self):
        return True, super().help_messager(super().general_commands()), "help"
