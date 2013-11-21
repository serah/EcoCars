/*
 * SimpleModal Basic Modal Dialog
 * http://simplemodal.com
 *
 * Copyright (c) 2013 Eric Martin - http://ericmmartin.com
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 */

jQuery(function ($) {
	// Load dialog on page load
	//$('#basic-modal-content').modal();

	// Load dialog on click
	$('#basic-modal-1 .basic').click(function (e) {
		$('#basic-modal-content-1').modal();

		return false;
});

});

jQuery(function ($) {
    // Load dialog on page load
    //$('#basic-modal-content').modal();

    // Load dialog on click
    $('#basic-modal-2 .basic').click(function (e) {
        $('#basic-modal-content-2').modal();

        return false;
    });

});

jQuery(function ($) {
    // Load dialog on page load
    //$('#basic-modal-content').modal();

    // Load dialog on click
    $('#basic-modal-3 .basic').click(function (e) {
        $('#basic-modal-content-3').modal();

        return false;
    });

});