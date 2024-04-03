from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required

def feedback_list(request):
  feedbacks = Feedback.objects.all().order_by('-publish_date')  # Order by most recent
  context = {'feedbacks': feedbacks}
  return render(request, 'feedback_list.html', context)

#@login_required
def feedback_create(request):
  if request.method == 'POST':
    event_id = request.POST.get('event_id')  # Get event ID from form
    feedback_text = request.POST.get('feedback_text')
    user = request.user  # Get currently logged-in user

    new_feedback = Feedback.objects.create(
        event=Event.objects.get(pk=event_id),  # Retrieve Event object
        feedback_text=feedback_text,
        user=user
    )
    return redirect('feedback_list')  # Redirect to feedback list after creation
  else:
    # Handle GET request (e.g., display a form)
    return render(request, 'feedback_create.html')

def feedback_detail(request, feedback_id):
  try:
    feedback = Feedback.objects.get(pk=feedback_id)
    context = {'feedback': feedback}
    return render(request, 'feedback_detail.html', context)
  except Feedback.DoesNotExist:
    # Handle feedback not found case (e.g., display error message)
    return render(request, 'feedback_not_found.html')

#@login_required
def feedback_update(request, feedback_id):
  try:
    feedback = Feedback.objects.get(pk=feedback_id)
    if request.method == 'POST':
      feedback_text = request.POST.get('feedback_text')  # Get updated feedback text

      feedback.feedback_text = feedback_text
      feedback.save()
      return redirect('feedback_detail', feedback_id)  # Redirect to detail after update
    else:
      context = {'feedback': feedback}
      return render(request, 'feedback_update.html', context)  # Display update form
  except Feedback.DoesNotExist:  # Use the full exception name
      # Handle feedback not found case (e.g., display error message)
      return render(request, 'feedback_not_found.html')

def feedback_delete(request, feedback_id):
  try:
    feedback = Feedback.objects.get(pk=feedback_id)
    if request.method == 'POST':
      feedback.delete()
      return redirect('feedback_list')  # Redirect to feedback list after deletion
    else:
      # Display confirmation message before deletion (optional)
      context = {'feedback': feedback}
      return render(request, 'feedback_delete_confirm.html', context)
  except Feedback.DoesNotExist:
    # Handle feedback not found case (e.g., display error message)
    return render(request, 'feedback_not_found.html')




########################################################for ionic app############################################

#
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import Feedback  # Replace with your model
#
# def feedback_list(request):
#     feedbacks = Feedback.objects.all().order_by('-publish_date')
#     # Convert feedback objects to a list of dictionaries
#     data = [feedback.to_dict() for feedback in feedbacks]
#     return JsonResponse(data, safe=False)  # Set safe=False for nested serializers
#
# def feedback_detail(request, feedback_id):
#     feedback = get_object_or_404(Feedback, pk=feedback_id)
#     return JsonResponse(feedback.to_dict(), safe=False)
#
# @login_required  # Add if you need authentication
# def feedback_create(request):
#     if request.method == 'POST':
#         # Parse request data (likely from JSON body)
#         data = json.loads(request.body)
#         # Validate and process data
#         new_feedback = Feedback.objects.create(**data)  # Unpack dictionary to model fields
#         return JsonResponse(new_feedback.to_dict(), safe=False)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
#
# @login_required  # Add if you need authentication
# def feedback_update(request, feedback_id):
#     feedback = get_object_or_404(Feedback, pk=feedback_id)
#     if request.method == 'PUT':
#         # Parse request data (likely from JSON body)
#         data = json.loads(request.body)
#         # Validate and update feedback object
#         for field, value in data.items():
#             setattr(feedback, field, value)
#         feedback.save()
#         return JsonResponse(feedback.to_dict(), safe=False)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
#
# @login_required  # Add if you need authentication
# def feedback_delete(request, feedback_id):
#     feedback = get_object_or_404(Feedback, pk=feedback_id)
#     if request.method == 'DELETE':
#         feedback.delete()
#         return JsonResponse({'message': 'Feedback deleted successfully'})
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
