from django import forms
from .models import Lead

class LeadForm(forms.ModelForm): # ka mek el sovorakan /Form/, bayc qani vor menq uzum enq arden
                                 # arka modeli himan vra karucenq mer formy aranc gemmoroyi,
                                 # ayd isk patcharov menq ogtagorcum enq /ModelForm/ u ira mejic
                                 # /Meta/ configuracion classic enq ogtvum, vortex nshum enq
                                 # /model/-y, vori vra himnvelu a formy u et modeli miji parametreric
                                 # mi qanisy - /firlds/, vory vor petq a nermucvi useri koxmic,
                                 # vory che, aysinqn djangon a viz dnelu - rad.
    class Meta:
        model = Lead # es qez modely vori vra himnvelu a formy.
        fields = ['name', 'contact', 'message'] # es el qez mer axper useri koxmic nermucvox
                                                # parametrery /list[str]/ tarberakov brats.
