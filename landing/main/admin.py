from django.contrib import admin
from .models import Lead # mtcnum enq mer modelin admini kipishi mej

# Register your models here.

@admin.register(Lead) # grancum enq mer modelchikin adminum
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'created_at') # vonc a cuyc talu thumbnail-y
                                                     # (nu aranc message eli, te che
                                                     # shat erkar klner thumbanail-y axper)
    search_fields = ('name', 'contact', 'message') # vor parametrerov karanq poisk tanq Lead-erin
    readonly_fields = ('created_at',) # ay es field-y daje adminy chi kara poxi arden,
                                     # vortev jamanak a axper, isk jamanaki het chen xaxum axpers
