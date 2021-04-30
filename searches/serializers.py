from drf_haystack.serializers import HaystackSerializer

from .search_indexes import LocationIndex


class LocationSerializer(HaystackSerializer):
    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [LocationIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = ["text", "address", "city", "zip_code", "autocomplete"]
