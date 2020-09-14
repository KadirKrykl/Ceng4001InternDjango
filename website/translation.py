from modeltranslation.translator import register, TranslationOptions
from .models import ResearchGroups, News, UserProfile, Project, Resource, Publication, Research

@register(ResearchGroups)
class ResearchGroupsTranslationOptions(TranslationOptions):
    fields = ('title', 'information')
    
@register(UserProfile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('information',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')

@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('title', 'information')

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'information')

@register(Research)
class ResearchTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')