from django.db import models

# Create your models here.


class Catalog(models.Model):
    href = models.CharField(max_length=200, blank=True)
    version = models.CharField(max_length=200, default="", blank=True)
    lastUpdate = models.DateTimeField(default=None, blank=True)
    validFor_startDateTime = models.DateTimeField(default=None, blank=True)
    validFor_endDateTime = models.DateTimeField(default=None, blank=True)
    lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
    type = models.CharField(max_length=200, default=None, blank=True)


class Category(models.Model):
    href = models.CharField(max_length=200, blank=True)
    version = models.CharField(max_length=200, default="", blank=True, null=True)
    lastUpdate = models.DateTimeField(default=None, blank=True, null=True)
    validFor_startDateTime = models.CharField(max_length=200, default=None, blank=True, null=True)
    validFor_endDateTime = models.CharField(max_length=200, default=None, blank=True, null=True)
    lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
    parentId = models.CharField(max_length=200, default="")
    isRoot = models.BooleanField(default=False)
    name = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    catalog = models.ForeignKey(Catalog, related_name='category', on_delete=models.CASCADE, default=None, blank=True, null=True)


class RelatedParty(models.Model):
    href = models.CharField(max_length=200, blank=True, unique=True)
    validFor_startDateTime = models.CharField(max_length=200, default=None, blank=True, null=True)
    validFor_endDateTime = models.CharField(max_length=200, default=None, blank=True, null=True)
    name = models.TextField(default='', blank=True)
    role = models.CharField(max_length=200, default="", blank=True, null=True)
    catalog = models.ForeignKey(Catalog, related_name='relatedParty', on_delete=models.CASCADE, default=None, blank=True, null=True)
# class Channel(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)


# class Place(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)


# class Price(models.Model):
#     currencyCode = models.CharField(max_length=5, default="", blank=True)
#     dutyFreeAmount = models.CharField(max_length=200, default="", blank=True)
#     percentage = models.CharField(max_length=3, default="", blank=True)
#     taxIncludedAmount = models.CharField(max_length=200, default="", blank=True)
#     priceType = models.CharField(max_length=10, default="", blank=True)
#     taxRate = models.CharField(max_length=200, default="", blank=True)


# class ProductOfferPriceAlteration(models.Model):
#     applicationDuration = models.CharField(max_length=200, default="", blank=True)
#     description = models.TextField(default='', blank=True)
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     priceCondition = models.TextField(default='', blank=True)
#     priceType = models.CharField(max_length=10, default="", blank=True)
#     recurringChargePeriod = models.CharField(max_length=200, default="", blank=True)
#     unitOfMeasure = models.CharField(max_length=200, default="", blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)

    
# class ProductOfferingPrice(models.Model):
#     recurringChargePeriod = models.CharField(max_length=200, default="", blank=True)
#     unitOfMeasure = models.CharField(max_length=200, default="", blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     description = models.TextField(default='', blank=True)
#     name = models.TextField(default='', blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)
#     priceType = models.CharField(max_length=10, default="", blank=True)
#     price = models.ForeignKey(Price, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     productOfferPriceAlteration = models.ForeignKey(ProductOfferPriceAlteration, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    
# class ProductOfferingTerm(models.Model):
#     description = models.TextField(default='', blank=True)
#     duration = models.CharField(max_length=200, default="", blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     name = models.TextField(default='', blank=True)


# class ProductSpecification(models.Model):
#     description = models.TextField(default='', blank=True)
#     brand = models.CharField(max_length=200, default="", blank=True)
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     isBundle = models.BooleanField(default=False, blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)
#     lastUpdate = models.DateTimeField(default=None, blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
#     productNumber = models.CharField(max_length=200, default="", blank=True)


# class ServiceCandidate(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)
#     lastUpdate = models.DateTimeField(default=None, blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
#     name = models.TextField(default='', blank=True)
#     description = models.TextField(default='', blank=True)
    

# class ServiceLevelAgreement(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)


# class ResourceCandidate(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)


# class Attachment(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     type = models.CharField(max_length=200, default="", blank=True)
#     url = models.CharField(max_length=200, default="", blank=True)


# class ProductSpecCharacteristicValue(models.Model):
#     default = models.BooleanField(default=True, blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     valueType = models.CharField(max_length=200, default="", blank=True)
#     value = models.CharField(max_length=200, default="", blank=True)
#     unitOfMeasure = models.CharField(max_length=200, default="", blank=True)
#     valueFrom = models.CharField(max_length=200, default="", blank=True)
#     valueTo = models.CharField(max_length=200, default="", blank=True)


# class ProductSpecCharacteristic(models.Model):
#     configurable = models.BooleanField(default=False, blank=True)
#     description = models.TextField(default='', blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     valueType = models.CharField(max_length=200, default="", blank=True)
#     productSpecCharacteristicValue = models.ForeignKey(ProductSpecCharacteristicValue, on_delete=models.CASCADE, default=None, null=True, blank=True)


# class ProductSpecificationRelationship(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     type = models.CharField(max_length=200, default="", blank=True)


# class ResourceSpecification(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)


# class ServiceSpecification(models.Model):
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)


# class BundledProductSpecification(models.Model):
#     brand = models.CharField(max_length=200, default="", blank=True)
#     description = models.TextField(default='', blank=True)
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     isBundle = models.BooleanField(default=False, blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)
#     lastUpdate = models.DateTimeField(default=None, blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
#     productNumber = models.CharField(max_length=200, default="", blank=True)


# class ProductOffering(models.Model):
#     description = models.TextField(default='', blank=True)
#     href = models.CharField(max_length=200, default="", blank=True)
#     name = models.TextField(default='', blank=True)
#     isBundle = models.BooleanField(default=False, blank=True)
#     version = models.CharField(max_length=200, default="", blank=True)
#     lastUpdate = models.DateTimeField(default=None, blank=True)
#     validFor = models.ForeignKey(ValidFor, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     lifecycleStatus = models.CharField(max_length=10, default=None, null=True, blank=True)
#     place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     channel = models.ForeignKey(Channel, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     serviceCandidate = models.ForeignKey(ServiceCandidate, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     resourceCandidate = models.ForeignKey(ResourceCandidate, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     productOfferingTerm = models.ForeignKey(ProductOfferingTerm, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     productOfferingPrice = models.ForeignKey(ProductOfferingPrice, on_delete=models.CASCADE, default=None, null=True, blank=True)
