# from django.shortcuts import render
# from.models import Movies
# from django.http import JsonResponse

# def movies_list(request):
#     movies = Movies.objects.all()
#     data = {
#         'movies' : list(movies.values())
#         }
#     return JsonResponse(data)
#     # return render(request,'movies_list.html', {'movies': movies})


# def movies_detail(request, pk):
#     movie = Movies.objects.get(pk=pk)
#     data = {
        
#         'movie' : movie.name,
#         'description' : movie.description,
#         'active' : movie.active,
#     }
#     print(movie.name)
#     return JsonResponse(data)
#     # return render(request,'movies_detail.html', {'movie': movie})