from rest_framework import serializers

from ...models import ContactModel
from ...serializers.contact.sendmessage import send_telegram_message 

class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        exclude = [
            "created_at",
            "updated_at",
        ]

import logging

logger = logging.getLogger(__name__)


class ListContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class RetrieveContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class CreateContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta):
        pass
        
    def create(self, validated_data):
        contact = ContactModel.objects.create(**validated_data)
        
        def user_message(**kwargs):
            message_text = ''
            
            message_text += f"💌 Yangi xabar\n\n"
            message_text += f"👤 Ism: {kwargs['name']}\n" 
            message_text += f"📩 Mavzu: {kwargs['subject']}\n" 
            message_text += f"💬 Xabar: {kwargs['message']}\n"
            
            return message_text 
        
        message = user_message(
            name=contact.name,
            subject=contact.subject,
            message=contact.message
        )
        
        response = send_telegram_message(message)
        
        if response and 'ok' in response and response['ok'] == True:
            logger.info("Xabar muvaffaqiyatli yuborildi.")
        else:
            print(response)
            logger.error("Xabar yuborishda xatolik yuz berdi.")
        
        return contact

                
