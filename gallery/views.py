from django.http import HttpResponse
import json
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.utils import get_page_range
from .models import Photo, Video


def gallery_video(request, page_number=1):
    videos = Video.objects.all()
    page = request.GET.get('page', page_number)
    paginator = Paginator(videos, 2)

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    index = videos.number - 1
    max_index = len(paginator.page_range)

    start_index, end_index = get_page_range(index, max_index)

    page_range = list(paginator.page_range)[start_index:end_index]


    ###
    pagination_html = ''
    if videos.paginator.num_pages > 1:
        pagination_html = '<div class="pagination pagination_has-padding_top">'

        if videos.number > 1:
            if videos.number-1 == 1:
                pagination_html += '<a class="pagination__prev js-video-gallery-ajax-link" ' \
                                   'href="' + request.path + '"><i class="icon icon_arrow_type-2"></i></a>'
            else:
                pagination_html += '<a class="pagination__prev js-video-gallery-ajax-link" ' \
                                   'href="'+request.path+'?page=' + str(videos.number - 1) + '"><i class="icon icon_arrow_type-2"></i></a>'

        if start_index > 0:
            pagination_html += '<a class="pagination__first js-video-gallery-ajax-link" ' \
                               'href="' + request.path + '">Первая</a>'

        pagination_html += '<div class="pagination__list">'

        for i in page_range:
            if videos.number == i:
                pagination_html += '<a class="pagination__item pagination__item_active" ' \
                                   'href="#">' + str(i) + '</a>'
            elif i == 1:
                pagination_html += '<a class="pagination__item js-video-gallery-ajax-link" ' \
                                   'href="' + request.path + '">1</a>'
            else:
                pagination_html += '<a class="pagination__item js-video-gallery-ajax-link" ' \
                                   'href="'+request.path+'?page=' + str(i) + '">' + str(i) + '</a>'

        pagination_html += '</div>'

        if end_index < videos.paginator.num_pages:
            pagination_html += '<a class="pagination__last js-video-gallery-ajax-link" ' \
                               'href="'+request.path+'?page=' + str(videos.paginator.num_pages) + '">Последняя</a>'
        if videos.number != videos.paginator.num_pages:
            pagination_html += '<a class="pagination__next js-video-gallery-ajax-link" ' \
                               'href="'+request.path+'?page=' + str(videos.number + 1) + '">' \
                                '<i class="icon icon_arrow_type-2"></i></a>'

        pagination_html += '</div>'
    ###
    if request.is_ajax():
        videos_choices = [dict(title=video.title,
                               video_id=video.videoId,
                               properties=list(video.videoproperty_set.all().values('property', 'description'))) for video in videos]

        videos_choices[0]['pagination_html'] = pagination_html

        print([list(video.videoproperty_set.all().values('property', 'description')) for video in videos])

        return HttpResponse(
            json.dumps(
                videos_choices,
                ensure_ascii=False),  # for russian
            content_type='application/json',
        )


    context = {
        "videos": videos,
        #"page_range": page_range,
        "pagination_html": pagination_html
    }
    return render(request, "gallery/gallery-video.html", context)


def gallery_photo(request, slug, page_number=1):
    photos = Photo.objects.filter(category__slug=slug)
    page = request.GET.get('page', page_number)
    paginator = Paginator(photos, 3)

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    index = photos.number - 1
    max_index = len(paginator.page_range)

    start_index, end_index = get_page_range(index, max_index)
    page_range = list(paginator.page_range)[start_index:end_index]

    ###
    pagination_html = ''
    if photos.paginator.num_pages > 1:
        pagination_html = '<div class="pagination pagination_has-padding_top">'

        if photos.number > 1:
            if photos.number-1 == 1:
                pagination_html += '<a class="pagination__prev js-photo-gallery-ajax-link" ' \
                                   'href="' + request.path + '"><i class="icon icon_arrow_type-2"></i></a>'
            else:
                pagination_html += '<a class="pagination__prev js-photo-gallery-ajax-link" ' \
                                   'href="'+request.path+'?page=' + str(photos.number - 1) + '"><i class="icon icon_arrow_type-2"></i></a>'

        if start_index > 0:
            pagination_html += '<a class="pagination__first js-photo-gallery-ajax-link" ' \
                               'href="' + request.path + '">Первая</a>'

        pagination_html += '<div class="pagination__list">'

        for i in page_range:
            if photos.number == i:
                pagination_html += '<a class="pagination__item pagination__item_active" ' \
                                   'href="#">' + str(i) + '</a>'
            elif i == 1:
                pagination_html += '<a class="pagination__item js-photo-gallery-ajax-link" ' \
                                   'href="' + request.path + '">1</a>'
            else:
                pagination_html += '<a class="pagination__item js-photo-gallery-ajax-link" ' \
                                   'href="'+request.path+'?page=' + str(i) + '">' + str(i) + '</a>'

        pagination_html += '</div>'

        if end_index < photos.paginator.num_pages:
            pagination_html += '<a class="pagination__last js-photo-gallery-ajax-link" ' \
                               'href="'+request.path+'?page=' + str(photos.paginator.num_pages) + '">Последняя</a>'
        if photos.number != photos.paginator.num_pages:
            pagination_html += '<a class="pagination__next js-photo-gallery-ajax-link" ' \
                               'href="'+request.path+'?page=' + str(photos.number + 1) + '">' \
                                '<i class="icon icon_arrow_type-2"></i></a>'

        pagination_html += '</div>'
    ###
    if request.is_ajax():
        photos_choices = [dict(caption=photo.caption,
                               thumbnail=photo.thumbnail.url,
                               picture=photo.picture.url,
                               size=str(photo.picture.width) + 'x' + str(photo.picture.height)) for photo in photos]

        photos_choices[0]['pagination_html'] = pagination_html



        return HttpResponse(
            json.dumps(
                photos_choices,
                ensure_ascii=False),  # for russian
            content_type='application/json',
        )


    context = {
        "photos": photos,
        # 'page_range': page_range,
        'pagination_html': pagination_html
    }
    return render(request, "gallery/gallery-photo.html", context)


