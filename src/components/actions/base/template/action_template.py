from components.actions.base.action import Action


class TemplateActionClass(Action):
    def __init__(self):
        super().__init__()

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)
        """
        Custom run method. Add your custom logic here.
        """
        print(self.name, '---> action has run!')


template_action = TemplateActionClass()