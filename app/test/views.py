import os
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Invoice

@csrf_exempt
def generate_invoice_xml(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        invoice = Invoice.objects.create(
            invoice_number=json_data['invoice_number'],
            customer_name=json_data['customer_name'],
            invoice_format=json_data['invoice_format']
        )

        template_name = f'invoice_format{invoice.invoice_format}.xml'
        template_path = os.path.join('/Users/someshkhade/Desktop/xml', template_name)

        # Debugging: Print template_path to verify the constructed path
        print("Template Path:", template_path)

        if os.path.exists(template_path):
            with open(template_path, 'r') as template_file:
                xml_content = template_file.read()

            xml_content = xml_content.format(invoice_number=invoice.invoice_number)

            response = HttpResponse(xml_content, content_type='application/xml')
            response['Content-Disposition'] = f'attachment; filename=invoice_{invoice.invoice_number}.xml'
            return response
        else:
            # Debugging: Print the directory contents to verify the file presence
            print("Directory Contents:", os.listdir('/Users/someshkhade/Desktop/xml'))
            return HttpResponse("Template file not found", status=404)
