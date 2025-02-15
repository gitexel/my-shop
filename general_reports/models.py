from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profitability(models.Model):
    date = models.DateField(_("date"), null=True, blank=True)
    type = models.CharField(_("type"), max_length=20, default="sales")
    value = models.DecimalField(
        _("Value"), max_digits=19, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = _("Profitability")
        verbose_name_plural = _("Profitability")
        managed = False
        db_table = "profitability_view"

        """
            create or replace view profitability_view as
            select "expensetransaction" as type, date, value
            from expense_expensetransaction
            
            union all
            select "saletransaction", date, value
            from sales_sale;
        """
