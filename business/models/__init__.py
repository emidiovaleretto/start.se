from django.db import models

TIME_EXISTENCE_CHOICES = (
    ('-6', 'Less than 6 months'),
    ('+6', 'More than 6 months'),
    ('+1', 'More than 1 year'),
    ('+5', 'More than 5 years')
)

STAGE_CHOICES = (
    ('I', 'I only have an idea'),
    ('MVP', 'I have an MVP'),
    ('MVPP', 'I have an MVP with paying customers'),
    ('E', 'Company ready to scale'),
)

AREA_CHOICES = (
    ('ED', 'Ed-tech'),       
    ('FT', 'Fintech'),        
    ('HC', 'Health-tech'),    
    ('BI', 'Bio-tech'),       
    ('IT', 'IT Services'),    
    ('RE', 'Real Estate'),    
    ('EN', 'Energy'),         
    ('AI', 'AI/ML'), 
    ('SA', 'SaaS'), 
)

from .Companies import Company